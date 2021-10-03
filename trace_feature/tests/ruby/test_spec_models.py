import pytest
import json
import os
from trace_feature.core.ruby.spec_models import It

class TestItInstance:
  @pytest.fixture
  def it_attributes(self):
    '''Returns a dictionary of attributes for a it'''

    attributes = {
      'line': 10,
      'description': 'Some description',
      'file': '/home/user/documents/example-project/app/models/file_example.rb',
      'executed_methods': ['index', 'create']
    }
    return attributes

  @pytest.fixture
  def empty_it(self):
    '''Returns a It with empty or blank attributes'''
    return It()

  @pytest.fixture
  def it(self, it_attributes):
    '''Returns a It with setted attributes'''
    return It(line=it_attributes['line'],
              description=it_attributes['description'],
              file=it_attributes['file'],
              executed_methods=it_attributes['executed_methods'])

  def test_default_initial_attributes(self, empty_it):
    assert empty_it.line == None
    assert empty_it.description == ''
    assert empty_it.file == ''
    assert empty_it.executed_methods == []

  def test_setting_attributes(self, it, it_attributes):
    assert it.line == it_attributes['line']
    assert it.description == it_attributes['description']
    assert it.file == it_attributes['file']
    assert it.executed_methods == it_attributes['executed_methods']

  def test_str_print(self, it, it_attributes):
    assert it.__str__() == it_attributes['description']

  def test_obj_dict(self, it):
    assert it.obj_dict() == it.__dict__
