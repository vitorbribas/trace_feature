import pytest
import os

from trace_feature.core.ruby.ruby_spec_execution import *

class TestRubySpecExecution:

  @pytest.fixture
  def utils_path(self):
    dir_path = os.path.dirname(__file__).split('ruby')[0]
    return os.path.join(dir_path, "utils")

  def test_get_its(self, utils_path):
    spec_file_path = utils_path + "/spec/user_spec.rb"
    its = get_its(spec_file_path)

    assert len(its) == 19
    assert all(map(lambda s: s.description != '', its))
    assert all(map(lambda s: s.line != None, its))
    assert all(map(lambda s: s.file != '', its))

  def test_read_specs(self, utils_path):
    specs = read_specs(utils_path)

    assert len(specs) == 30
    assert all(map(lambda s: s.description != '', specs))
    assert all(map(lambda s: s.line != None, specs))
    assert all(map(lambda s: s.file != '', specs))
