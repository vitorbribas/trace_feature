import pytest
import os
import json
import re
from unittest.mock import patch, mock_open

from trace_feature.core.ruby.ruby_config import RubyConfig

class TestRubyConfig:

  @pytest.fixture
  def config(self):
    return RubyConfig()

  @pytest.fixture
  def gemfile_path(self):
    dir_path = os.path.dirname(__file__).split('ruby')[0]
    return os.path.join(dir_path, "utils")

  def test_get_local_path(self, config):
    local_path_return = config.get_local_path()
    expected_return = '.'

    assert local_path_return == expected_return

  @patch('trace_feature.core.ruby.ruby_config.os')
  def test_is_rails_project(self, mocked_os, config):
    expected = mocked_os.path.exists.return_value = True
    actual = config.is_rails_project('.')

    assert mocked_os.path.exists.called
    assert expected == actual

  def test_is_test_group(self, config):
    dev_test_group_line = 'group :development, :test do'
    dev_group_line = 'group :development do'
    assertion_one = config.is_test_group(dev_test_group_line.split())
    assertion_two = config.is_test_group(dev_group_line.split())

    assert assertion_one == True
    assert assertion_two == False

  def test_simplecov_exists(self, config):
    simple_cov_line = "gem 'simplecov-json'"
    another_gem_line = "gem 'capybara'"
    assertion_one = config.simplecov_exists(simple_cov_line.split())
    assertion_two = config.simplecov_exists(another_gem_line.split())

    assert assertion_one == True
    assert assertion_two == False

  def test_require_simple_cov(self, config):
    simple_cov_line = "require 'simplecov-json'"
    another_file_line = "require 'cucumber/rails'"
    assertion_one = config.req_simple_cov(simple_cov_line.split())
    assertion_two = config.req_simple_cov(another_file_line.split())

    assert assertion_one == True
    assert assertion_two == False

  def test_simple_cov_start(self, config):
    simple_cov_line = "SimpleCov.start 'rails'"
    another_file_line = ""
    assertion_one = config.simple_cov_start(simple_cov_line.split())
    assertion_two = config.simple_cov_start(another_file_line.split())

    assert assertion_one == True
    assert assertion_two == False

  def test_simple_cov_exclude(self, config):
    simple_cov_line = "add_filter ['migrations', 'db', '.git', 'features']"
    another_file_line = ""
    assertion_one = config.simple_cov_exclude(simple_cov_line.split())
    assertion_two = config.simple_cov_exclude(another_file_line.split())

    assert assertion_one == True
    assert assertion_two == False

  def test_result_dir(self, config):
    simple_cov_line = "SimpleCov.coverage_dir 'coverage/cucumber'"
    another_file_line = ""
    assertion_one = config.result_dir(simple_cov_line.split())
    assertion_two = config.result_dir(another_file_line.split())

    assert assertion_one == True
    assert assertion_two == False

  def test_check_gemfile(self, config, gemfile_path):
    content = config.SIMPLECOV
    config.check_gemfile(gemfile_path)

    with open(gemfile_path + '/Gemfile', 'r+') as opened_file:
      lines = opened_file.readlines()
      assert content in lines

      # clean test changes on file example
      if content in lines:
        del lines[57]
        opened_file.seek(0)
        opened_file.truncate()
        opened_file.writelines(lines)

  def test_verify_requirements_without_simplecov(self, config, gemfile_path):
    content = config.SIMPLECOV
    ret = config.verify_requirements_on_gemfile(config, gemfile_path)

    with open(gemfile_path + '/Gemfile', 'r') as opened_file:
      lines = opened_file.readlines()
      assert content not in lines
      assert ret == False

  def test_verify_requirements_with_simplecov(self, config, gemfile_path):
    content = config.SIMPLECOV
    config.check_gemfile(gemfile_path)
    ret = config.verify_requirements_on_gemfile(config, gemfile_path)

    with open(gemfile_path + '/Gemfile', 'r+') as opened_file:
      lines = opened_file.readlines()
      assert content in lines
      assert ret == True

      # clean test changes on file example
      if content in lines:
        del lines[57]
        opened_file.seek(0)
        opened_file.truncate()
        opened_file.writelines(lines)

  def test_verify_requirements_without_reqsimcov(self, config, gemfile_path):
    content = config.REQSIMCOV
    ret = config.verify_requirements_on_env_file(config, gemfile_path)

    with open(gemfile_path + '/features/support/env.rb', 'r') as opened_file:
      lines = opened_file.readlines()
      assert content not in lines
      assert ret == False

  def test_verify_requirements_without_start(self, config, gemfile_path):
    content = config.START
    ret = config.verify_requirements_on_env_file(config, gemfile_path)

    with open(gemfile_path + '/features/support/env.rb', 'r') as opened_file:
      lines = opened_file.readlines()
      assert content not in lines
      assert ret == False

  def test_verify_requirements_without_result_dir(self, config, gemfile_path):
    content = config.RESULT_DIR
    ret = config.verify_requirements_on_env_file(config, gemfile_path)

    with open(gemfile_path + '/features/support/env.rb', 'r') as opened_file:
      lines = opened_file.readlines()
      assert content not in lines
      assert ret == False

  def test_verify_requirements_without_exclude_folders(self, config, gemfile_path):
    content = config.EXCLUDE_FOLDERS
    ret = config.verify_requirements_on_env_file(config, gemfile_path)

    with open(gemfile_path + '/features/support/env.rb', 'r') as opened_file:
      lines = opened_file.readlines()
      assert content not in lines
      assert ret == False

  def test_verify_requirements_with_complete_env_file(self, config, gemfile_path):
    config.check_environment(gemfile_path)
    ret = config.verify_requirements_on_env_file(config, gemfile_path)

    assert ret == True

    with open(gemfile_path + '/features/support/env.rb', 'r+') as opened_file:
      file_content = opened_file.read()

      # clean test changes on file example
      if (re.search(re.escape(config.REQSIMCOV),       file_content, flags=re.M) is not None and
          re.search(re.escape(config.START),           file_content, flags=re.M) is not None and
          re.search(re.escape(config.RESULT_DIR),      file_content, flags=re.M) is not None and
          re.search(re.escape(config.EXCLUDE_FOLDERS), file_content, flags=re.M) is not None):
        lines = file_content.split('\n')
        del lines[6:11]
        opened_file.seek(0)
        opened_file.truncate()
        opened_file.write('\n'.join(lines))
