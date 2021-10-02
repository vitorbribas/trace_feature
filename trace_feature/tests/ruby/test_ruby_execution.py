import json
import os
import re
import pytest

from trace_feature.core.ruby.ruby_execution import RubyExecution
from trace_feature.core.models import Feature
from trace_feature.core.ruby.spec_models import It

class TestRubyExecution:

  @pytest.fixture
  def ruby_execution(self):
    return RubyExecution()

  @pytest.fixture
  def file_path(self):
    base_path = os.path.dirname(__file__).split('ruby')[0]
    return os.path.join(base_path, "utils/methods/user.rb")

  @pytest.fixture
  def cov_result(self):
    base_path = os.path.dirname(__file__).split('ruby')[0]
    cov_result_file = os.path.join(base_path, "utils/methods/cov_result.json")
    return json.load(open(cov_result_file))

  @pytest.fixture
  def trace_feature_path(self):
    return os.path.dirname(__file__).split('/trace_feature/tests')

  def test_is_method(self, ruby_execution):
    method_line = 'def full_name'
    code_line = 'self.first_name + self.last_name'
    blank_line = ''

    assertion_one = ruby_execution.is_method(method_line)
    assertion_two = ruby_execution.is_method(code_line)
    assertion_three = ruby_execution.is_method(blank_line)

    assert assertion_one == True
    assert assertion_two == False
    assert assertion_three == False

  def test_is_class(self, ruby_execution):
    class_line = 'class User'
    code_line = 'self.first_name + self.last_name'
    blank_line = ''

    assertion_one = ruby_execution.is_class(class_line)
    assertion_two = ruby_execution.is_class(code_line)
    assertion_three = ruby_execution.is_class(blank_line)

    assert assertion_one == True
    assert assertion_two == False
    assert assertion_three == False

  def test_get_method_or_class_name(self, ruby_execution, file_path):
    assertion_one = ruby_execution.get_method_or_class_name(1, file_path)
    assertion_two = ruby_execution.get_method_or_class_name(60, file_path)
    assertion_three = ruby_execution.get_method_or_class_name(41, file_path)

    assert assertion_one == 'User'
    assert assertion_two == 'valid_cpf'
    assert assertion_three == 'nth_validation_digit'

  def test_get_class_definition_line(self, ruby_execution, file_path):
    with open(file_path) as opened_file:
      ruby_execution.get_class_definition_line(opened_file)

      assert ruby_execution.class_definition_line == 1

  def test_get_executed_method_definition_lines(self, ruby_execution, file_path, cov_result):
    with open(file_path) as opened_file:
      key = file_path.split('methods/')[1]
      ruby_execution.get_executed_method_definition_lines(opened_file,
                                                 file_path,
                                                 cov_result['RSpec']['coverage'][key])

      assert ruby_execution.method_definition_lines == [41, 60, 75, 82, 87, 94]

  def test_get_executed_method_definition_lines(self, ruby_execution, file_path, cov_result):
    lines = [41, 60, 75, 82, 87, 94, 99, 104]

    with open(file_path) as opened_file:
      executed_lines = []
      key = file_path.split('methods/')[1]
      for n_line in lines:
        ret = ruby_execution.was_executed(n_line - 1, file_path, cov_result['RSpec']['coverage'][key])
        executed_lines.append(ret)

      assert executed_lines == [True, True, True, True, True, True, True, True]

  def test_is_empty_class(self, file_path, ruby_execution):
    content_path = os.path.dirname(__file__).split('ruby')[0]
    content_path = os.path.join(content_path, "utils/methods/application_helper.rb")

    with open(content_path) as opened_file:
      ret = ruby_execution.is_empty_class(opened_file)

      assert ret is True

    with open(file_path) as opened_file:
      ret = ruby_execution.is_empty_class(opened_file)

      assert ret is False

  def test_send_information(self, ruby_execution, requests_mock):
    json_string = json.dumps(ruby_execution.feature, default=Feature.obj_dict)
    requests_mock.post("http://localhost:8000/createproject", json=json_string)
    resp = ruby_execution.send_information(True)
    assert resp == 200

    json_string = json.dumps(ruby_execution.it_spec, default=It.obj_dict)
    requests_mock.post("http://localhost:8000/covrel/update_spectrum", json=json_string)
    resp = ruby_execution.send_information(False)
    assert resp == 200

  def test_get_project_name(self, ruby_execution, trace_feature_path):
    project_name = ruby_execution.get_project_name(trace_feature_path[0])

    assert project_name == 'trace_feature'

  def test_verify_git_repository(self, ruby_execution, trace_feature_path):
    github_url = ruby_execution.verify_git_repository(trace_feature_path[0])
    assert re.search(re.escape('https://github.com/'), github_url, flags=re.M) is not None

    github_url = ruby_execution.verify_git_repository(trace_feature_path[1])
    assert github_url is None

  def test_get_project_infos(self, ruby_execution, trace_feature_path):
    project = ruby_execution.get_project_infos(trace_feature_path[0])

    assert project.name == 'trace_feature'
    assert project.language == 'Ruby on Rails'
    assert re.search(re.escape('https://github.com/'), project.repository, flags=re.M) is not None
