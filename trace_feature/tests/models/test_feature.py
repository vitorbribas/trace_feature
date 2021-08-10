import pytest
import json
import os
from trace_feature.core.models import Feature

class TestFeatureInstance:
  @pytest.fixture
  def feature_attributes(self):
    '''Returns a dictionary of attributes for a feature'''
    base_path = os.path.dirname(__file__).split('models')[0]
    with open(os.path.join(base_path, "utils/parsed_feature_file.json")) as json_file:
      json_data = json.load(json_file)

    attributes = {
      'path_name': 'home/projects/diaspora',
      'feature_name': json_data['feature']['name'],
      'scenarios': json_data['feature']['children'][-2:],
      'language': json_data['feature']['language'],
      'user_story': 'blah',
      'tags': json_data['feature']['tags'],
      'line': json_data['feature']['location']['line'],
      'background': json_data['feature']['children'][0],
      'project': 'Diaspora',
    }
    return attributes

  @pytest.fixture
  def empty_feature(self):
    '''Returns a Feature with empty or blank attributes'''
    return Feature()

  @pytest.fixture
  def feature(self, feature_attributes):
    '''Returns a Feature with setted attributes'''
    return Feature(path_name=feature_attributes['path_name'],
                   feature_name=feature_attributes['feature_name'],
                   scenarios=feature_attributes['scenarios'],
                   language=feature_attributes['language'],
                   user_story=feature_attributes['user_story'],
                   tags=feature_attributes['tags'],
                   line=feature_attributes['line'],
                   background=feature_attributes['background'],
                   project=feature_attributes['project'])

  def test_default_initial_attributes(self, empty_feature):
    assert empty_feature.path_name == ""
    assert empty_feature.feature_name == ""
    assert empty_feature.scenarios == []
    assert empty_feature.language == ""
    assert empty_feature.user_story == ""
    assert empty_feature.tags == []
    assert empty_feature.line == None
    assert empty_feature.background == None
    assert empty_feature.project == ""

  def test_setting_attributes(self, feature, feature_attributes):
    assert feature.path_name == feature_attributes['path_name']
    assert feature.feature_name == feature_attributes['feature_name']
    assert feature.scenarios == feature_attributes['scenarios']
    assert feature.language == feature_attributes['language']
    assert feature.user_story == feature_attributes['user_story']
    assert feature.tags == feature_attributes['tags']
    assert feature.line == feature_attributes['line']
    assert feature.background == feature_attributes['background']
    assert feature.project == feature_attributes['project']

  def test_str_print(self, feature):
    assert feature.__str__() == feature.feature_name

  def test_obj_dict(self, feature):
    assert feature.obj_dict() == feature.__dict__
