import pytest
import json
import os
from trace_feature.core.models import Method

class TestMethodInstance:
  @pytest.fixture
  def method_attributes(self):
    '''Returns a dictionary of attributes for a method'''

    attributes = {
      'line': 2,
      'method_id': '/home/user/documents/example-project/app/models/file_example.rb' + 'example_method' + '2',
      'method_name': 'example_method',
      'class_name': 'Example',
      'class_path': '/home/user/documents/example-project/app/models/file_example.rb',
      'abc_score': 3,
      'complexity': 1,
      'number_of_lines': 5,
      'content': 'def example_method\n end\n\n',
    }
    return attributes

  @pytest.fixture
  def empty_method(self):
    '''Returns a Method with empty or blank attributes'''
    return Method()

  @pytest.fixture
  def method(self, method_attributes):
    '''Returns a Method with setted attributes'''
    return Method(line=method_attributes['line'],
                  method_id=method_attributes['method_id'],
                  method_name=method_attributes['method_name'],
                  class_name=method_attributes['class_name'],
                  class_path=method_attributes['class_path'],
                  abc_score=method_attributes['abc_score'],
                  complexity=method_attributes['complexity'],
                  number_of_lines=method_attributes['number_of_lines'],
                  content=method_attributes['content'])

  def test_default_initial_attributes(self, empty_method):
    assert empty_method.line == None
    assert empty_method.method_id == ""
    assert empty_method.method_name == ""
    assert empty_method.class_name == ""
    assert empty_method.class_path == ""
    assert empty_method.abc_score == 0
    assert empty_method.complexity == 0
    assert empty_method.number_of_lines == 0
    assert empty_method.content == ""

  def test_setting_attributes(self, method, method_attributes):
    assert method.line == method_attributes['line']
    assert method.method_id == method_attributes['method_id']
    assert method.method_name == method_attributes['method_name']
    assert method.class_name == method_attributes['class_name']
    assert method.class_path == method_attributes['class_path']
    assert method.abc_score == method_attributes['abc_score']
    assert method.complexity == method_attributes['complexity']
    assert method.number_of_lines == method_attributes['number_of_lines']
    assert method.content == method_attributes['content']

  def test_str_print(self, method):
    assert method.__str__() == ''

  def test_obj_dict(self, method):
    assert method.obj_dict() == method.__dict__
