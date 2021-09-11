import pytest
import os
import json
from unittest.mock import patch, mock_open

from trace_feature.core.ruby.ruby_config import RubyConfig

class TestRubyConfig:

  def test_get_local_path(self):
    ruby_config = RubyConfig()
    local_path_return = ruby_config.get_local_path()
    expected_return = '.'

    assert local_path_return == expected_return

  @patch('trace_feature.core.ruby.ruby_config.os')
  def test_is_rails_project(self, mocked_os):
    expected = mocked_os.path.exists.return_value = True
    actual = RubyConfig().is_rails_project('.')

    assert mocked_os.path.exists.called
    assert expected == actual

  def test_is_test_group(self):
    dev_test_group_line = 'group :development, :test do'
    dev_group_line = 'group :development do'
    assertion_one = RubyConfig().is_test_group(dev_test_group_line.split())
    assertion_two = RubyConfig().is_test_group(dev_group_line.split())

    assert assertion_one == True
    assert assertion_two == False

  def test_simplecov_exists(self):
    simple_cov_line = "gem 'simplecov-json'"
    another_gem_line = "gem 'capybara'"
    assertion_one = RubyConfig().simplecov_exists(simple_cov_line.split())
    assertion_two = RubyConfig().simplecov_exists(another_gem_line.split())

    assert assertion_one == True
    assert assertion_two == False

  def test_require_simple_cov(self):
    simple_cov_line = "require 'simplecov-json'"
    another_file_line = "require 'cucumber/rails'"
    assertion_one = RubyConfig().req_simple_cov(simple_cov_line.split())
    assertion_two = RubyConfig().req_simple_cov(another_file_line.split())

    assert assertion_one == True
    assert assertion_two == False

  def test_simple_cov_start(self):
    simple_cov_line = "SimpleCov.start 'rails'"
    another_file_line = ""
    assertion_one = RubyConfig().simple_cov_start(simple_cov_line.split())
    assertion_two = RubyConfig().simple_cov_start(another_file_line.split())

    assert assertion_one == True
    assert assertion_two == False

  def test_simple_cov_exclude(self):
    simple_cov_line = "add_filter ['migrations', 'db', '.git', 'features']"
    another_file_line = ""
    assertion_one = RubyConfig().simple_cov_exclude(simple_cov_line.split())
    assertion_two = RubyConfig().simple_cov_exclude(another_file_line.split())

    assert assertion_one == True
    assert assertion_two == False

  def test_result_dir(self):
    simple_cov_line = "SimpleCov.coverage_dir 'coverage/cucumber'"
    another_file_line = ""
    assertion_one = RubyConfig().result_dir(simple_cov_line.split())
    assertion_two = RubyConfig().result_dir(another_file_line.split())

    assert assertion_one == True
    assert assertion_two == False

  def test_check_gemfile(self):
    dir_path = base_path = os.path.dirname(__file__).split('ruby')[0]
    dir_path = os.path.join(dir_path, "utils")

    content = RubyConfig().SIMPLECOV
    RubyConfig().check_gemfile(dir_path)

    with open(dir_path + '/Gemfile', 'r+') as opened_file:
      lines = opened_file.readlines()
      assert content in lines

      # clean test changes on file example
      if content in lines:
        del lines[57]
        opened_file.seek(0)
        opened_file.writelines(lines)
