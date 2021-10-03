import pytest
import json
import os
from gherkin.parser import Parser
from gherkin.token_scanner import TokenScanner
from trace_feature.core.models import Feature
from trace_feature.core.features.gherkin_parser import *

class TestGherkinParser:
  @pytest.fixture
  def feature_file_path(self):
    base_path = os.path.dirname(__file__).split('features')[0]
    return os.path.join(base_path, "utils/features/aspect_navigation.feature")

  @pytest.fixture
  def parsed_feature_file(self, feature_file_path):
    with open(feature_file_path) as file:
      file.seek(0)
      parser = Parser()
      return parser.parse(TokenScanner(file.read()))

  def test_get_scenario(self, feature_file_path, parsed_feature_file):
    scenario = get_scenario(feature_file_path, 12)
    parsed_scenario = [s for s in parsed_feature_file['feature']['children'] if s['location']['line'] == 12][0]

    assert scenario.scenario_title == parsed_scenario['name']

  def test_get_absent_scenario(self, feature_file_path, parsed_feature_file):
    scenario = get_scenario(feature_file_path, 10)
    parsed_scenario = [s for s in parsed_feature_file['feature']['children'] if s['location']['line'] == 10]

    assert scenario == None
    assert parsed_scenario == []

  def test_read_feature(self, feature_file_path, parsed_feature_file):
    feature = read_feature(feature_file_path)

    assert feature.path_name == feature_file_path
    assert feature.feature_name == parsed_feature_file['feature']['name']
    assert feature.language == parsed_feature_file['feature']['language']
    assert feature.tags == parsed_feature_file['feature']['tags']
    assert feature.line == parsed_feature_file['feature']['location']['line']

  def test_get_scenarios(self, parsed_feature_file):
    children = parsed_feature_file['feature']['children']
    scenarios = get_scenarios(children)
    children_names = [c['name'] for c in children]
    scenario_names = [s.scenario_title for s in scenarios]

    assert len(scenarios) == len(children)
    assert children_names == scenario_names

  def test_get_steps(self, parsed_feature_file):
    steps = parsed_feature_file['feature']['children'][0]['steps']
    all_steps = get_steps(steps)
    step_locations = [s['text'] for s in steps]
    all_step_locations = [a.text for a in all_steps]

    assert len(steps) == len(all_steps)
    assert step_locations == all_step_locations

  def test_read_all_bdds(self, feature_file_path):
    tests_path = os.path.dirname(__file__).split('features')[0]
    utils_folder = os.path.join(tests_path, "utils")

    features = read_all_bdds(utils_folder)
    feature = read_feature(feature_file_path)

    assert features[0].feature_name == feature.feature_name
    assert features[0].language == feature.language
    assert features[0].path_name == feature.path_name
    assert features[0].tags == feature.tags
    assert features[0].line == feature.line
