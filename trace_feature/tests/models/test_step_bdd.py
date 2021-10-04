import pytest
import json
import os
from trace_feature.core.models import StepBdd

class TestStepBddInstance:
  @pytest.fixture
  def parsed_feature_file(self):
    '''Returns a parsed feature file as json'''
    base_path = os.path.dirname(__file__).split('models')[0]
    with open(os.path.join(base_path, "utils/parsed_feature_file.json")) as json_file:
      return json.load(json_file)

  @pytest.fixture
  def step_bdd_attributes(self, parsed_feature_file):
    '''Returns a dictionary of attributes for a step_bdd'''

    step = parsed_feature_file['feature']['children'][0]['steps'][0]
    attributes = {
      'line': step['location']['line'],
      'keyword': step['keyword'],
      'text': step['text']
    }
    return attributes

  @pytest.fixture
  def empty_step_bdd(self):
    '''Returns a StepBdd with empty or blank attributes'''
    return StepBdd()

  @pytest.fixture
  def step_bdd(self, step_bdd_attributes):
    '''Returns a StepBdd with setted attributes'''
    return StepBdd(line=step_bdd_attributes['line'],
                   keyword=step_bdd_attributes['keyword'],
                   text=step_bdd_attributes['text'])

  def test_default_initial_attributes(self, empty_step_bdd):
    assert empty_step_bdd.line == None
    assert empty_step_bdd.keyword == ''
    assert empty_step_bdd.text == ''

  def test_setting_attributes(self, step_bdd, step_bdd_attributes):
    assert step_bdd.line == step_bdd_attributes['line']
    assert step_bdd.keyword == step_bdd_attributes['keyword']
    assert step_bdd.text == step_bdd_attributes['text']
