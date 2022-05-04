import pytest
from trace_feature.core.models.project import Project

class TestProjectInstance:
  @pytest.fixture
  def project_attributes(self):
    '''Returns a dictionary of attributes for a project'''
    attributes = {
      'project_name': 'Diaspora',
      'language_name': 'Ruby on Rails',
      'repository_name': 'https://github.com/BDD-OperationalProfile/trace_feature',
      'methods_collection': ['index', 'create']
    }
    return attributes

  @pytest.fixture
  def empty_project(self):
    '''Returns a Project with empty or blank attributes'''
    return Project()

  @pytest.fixture
  def project(self, project_attributes):
    '''Returns a Project with setted attributes'''
    return Project(name=project_attributes['project_name'],
                   language=project_attributes['language_name'],
                   repository=project_attributes['repository_name'],
                   methods=project_attributes['methods_collection'])

  def test_default_initial_attributes(self, empty_project):
    assert empty_project.name == ''
    assert empty_project.language == ''
    assert empty_project.repository == ''
    assert empty_project.methods == []

  def test_setting_attributes(self, project, project_attributes):
    assert project.name == project_attributes['project_name']
    assert project.language == project_attributes['language_name']
    assert project.repository == project_attributes['repository_name']
    assert project.methods == project_attributes['methods_collection']

  def test_str_print(self, project):
    assert project.__str__() == ''

  def test_obj_dict(self, project):
    assert project.obj_dict() == project.__dict__
