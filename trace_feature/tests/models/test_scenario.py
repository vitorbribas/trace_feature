import pytest
import json
import os
from trace_feature.core.models import SimpleScenario, StepBdd

class TestSimpleScenarioInstance:
  @pytest.fixture
  def parsed_feature_file(self):
    '''Returns a parsed feature file as json'''
    base_path = os.path.dirname(__file__).split('models')[0]
    with open(os.path.join(base_path, "utils/parsed_feature_file.json")) as json_file:
      return json.load(json_file)

  @pytest.fixture
  def steps(self, parsed_feature_file):
    '''Returns a Step with setted attributes'''
    all_steps = []
    for each_step in parsed_feature_file['feature']['children'][0]['steps']:
      step = StepBdd(line=each_step['location']['line'],
                     keyword=each_step['keyword'],
                     text=each_step['text'])
      all_steps.append(step)

    return all_steps

  @pytest.fixture
  def scenario_attributes(self, parsed_feature_file, steps):
    '''Returns a dictionary of attributes for a scenario'''

    attributes = {
      'steps': steps,
      'scenario_title': parsed_feature_file['feature']['children'][0]['name'],
      'line': parsed_feature_file['feature']['children'][0]['location']['line'],
      'executed_methods': ['index', 'show']
    }
    return attributes

  @pytest.fixture
  def empty_scenario(self):
    '''Returns a SimpleScenario with empty or blank attributes'''
    return SimpleScenario()

  @pytest.fixture
  def scenario(self, scenario_attributes):
    '''Returns a SimpleScenario with setted attributes'''
    return SimpleScenario(steps=scenario_attributes['steps'],
                          scenario_title=scenario_attributes['scenario_title'],
                          line=scenario_attributes['line'],
                          executed_methods=scenario_attributes['executed_methods'])

  def test_default_initial_attributes(self, empty_scenario):
    assert empty_scenario.steps == []
    assert empty_scenario.scenario_title == ''
    assert empty_scenario.line == None
    assert empty_scenario.executed_methods == []

  def test_setting_attributes(self, scenario, scenario_attributes):
    assert scenario.steps == scenario_attributes['steps']
    assert scenario.scenario_title == scenario_attributes['scenario_title']
    assert scenario.line == scenario_attributes['line']
    assert scenario.executed_methods == scenario_attributes['executed_methods']

  def test_str_print(self, scenario):
    assert scenario.__str__() == ''
