import pytest
import os

from trace_feature.core.ruby.ruby_execution import RubyExecution

class TestRubyExecution:

  @pytest.fixture
  def ruby_execution(self):
    return RubyExecution()

  @pytest.fixture
  def file_path(self):
    base_path = os.path.dirname(__file__).split('ruby')[0]
    return os.path.join(base_path, "utils/methods/user.rb")

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

