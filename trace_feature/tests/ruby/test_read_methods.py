import pytest
import os
import json
import linecache
from types import SimpleNamespace
from trace_feature.core.models import Project, Method
from trace_feature.core.ruby.read_methods import (get_methods_line, install_excellent_gem,
                                                  send_all_methods, get_abc_score,
                                                  get_cyclomatic_complexity, get_number_of_lines,
                                                  get_content)
from trace_feature.core.ruby.ruby_execution import RubyExecution


class TestReadMethodsInstance:
  @pytest.fixture
  def methods_file_path(self):
    base_path = os.path.dirname(__file__).split('ruby')[0]
    return os.path.join(base_path, "utils/methods/user.rb")

  @pytest.fixture
  def abc_fixtures_file_path(self):
    base_path = os.path.dirname(__file__).split('ruby')[0]
    return os.path.join(base_path, "utils/excellent/abc_fixtures.json")

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

  @pytest.fixture
  def project_attributes(self, method):
    '''Returns a dictionary of attributes for a project'''
    attributes = {
      'project_name': 'Diaspora',
      'language_name': 'Ruby on Rails',
      'repository_name': 'https://github.com/BDD-OperationalProfile/trace_feature',
      'methods_collection': [method]
    }
    return attributes

  @pytest.fixture
  def project(self, project_attributes):
    '''Returns a Project with setted attributes'''
    return Project(name=project_attributes['project_name'],
                   language=project_attributes['language_name'],
                   repository=project_attributes['repository_name'],
                   methods=project_attributes['methods_collection'])

  @pytest.fixture
  def parsed_excellent_analysis(self, abc_fixtures_file_path):
    parsed_json = json.load(open(abc_fixtures_file_path))
    class_file = json.loads(json.dumps(parsed_json[0]), object_hook=lambda d: SimpleNamespace(**d))
    return class_file

  def test_get_methods_line(self, methods_file_path):
    ruby_exec = RubyExecution()
    with open(methods_file_path) as opened_file_path:
      method_lines = get_methods_line(opened_file_path, ruby_exec)
      assert method_lines == [41, 60, 75, 82, 87, 94, 99, 104]

  def test_send_all_methods(self, requests_mock, project):
    json_string = json.dumps(project, default=Project.obj_dict)
    requests_mock.post("http://localhost:8000/createmethods", json=json_string)
    resp = send_all_methods(project.methods, 'http://localhost:8000')
    assert resp == 200

  def test_abc_score(self, parsed_excellent_analysis):
    methods = parsed_excellent_analysis.methods
    abc_scores = []
    for read_method in methods:
      abc_scores.append(get_abc_score(parsed_excellent_analysis.result, read_method))
    assert abc_scores == [0, 18.027756377319946, 0, 0, 0, 0, 0]

  def test_get_cyclomatic_complexity(self, parsed_excellent_analysis):
    methods = parsed_excellent_analysis.methods
    cyclomatic_complexities = []
    for read_method in methods:
      cyclomatic_complexities.append(get_cyclomatic_complexity(parsed_excellent_analysis.result, read_method))
    assert cyclomatic_complexities == [3.0, 4.0, 1.0, 1.0, 1.0, 2.0, 0]

  def test_get_number_of_lines(self, parsed_excellent_analysis):
    methods = parsed_excellent_analysis.methods
    number_of_files_by_method = []
    for read_method in methods:
      number_of_files_by_method.append(get_number_of_lines(parsed_excellent_analysis.result, read_method))
    assert number_of_files_by_method == [13, 9, 5, 3, 3, 5, 0]

  def test_get_content(self, methods_file_path):
    with open(methods_file_path) as opened_file:
      method_content = get_content(41, methods_file_path)
      content = ""
      for line_number in [*range(41, 60)]:
        content += linecache.getline(methods_file_path, line_number)
        line_number += 1

      assert method_content == content
