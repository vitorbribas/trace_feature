"""
    Module which declares some classes as models
"""

from abc import ABC, abstractmethod


class Project:
    """
        Project object
    """
    def __init__(self):
        self.name = ""
        self.language = ""
        self.repository = ""
        self.methods = []

    def __str__(self):
        print('PROJETO:')
        print("\t name: " + self.name)
        print("\t language: " + self.language)
        print("\t Repository: " + str(self.repository))

        return ''

    def obj_dict(self):
        """ Return a dictionary or other mapping object. """
        return self.__dict__


class Feature:
    """
        Feature object
    """

    def __init__(self):
        self.path_name = ""
        self.feature_name = ""
        self.scenarios = []
        self.language = ""
        self.user_story = ""
        self.tags = []
        self.line = None
        self.background = None
        self.project = ""

    def __str__(self):
        return self.feature_name

    def obj_dict(self):
        """ Return a dictionary or other mapping object. """
        return self.__dict__


class Scenario(ABC):
    """ Scenario object """

    def __init__(self):
        self.steps = NotImplemented
        self.scenario_title = NotImplemented
        self.line = NotImplemented
        self.executed_methods = NotImplemented


    # @property
    # def steps(self):
    #     raise NotImplementedError

    # @property
    # def scenario_title(self):
    #     raise NotImplementedError

    # @property
    # def line(self):
    #     raise NotImplementedError

    @abstractmethod
    def execute(self):
        """ Execute scenario """
        pass

    @abstractmethod
    def set_line(self):
        """
            Set line
        """
        pass


class SimpleScenario(Scenario):
    """ Simple scenario object """

    def __init__(self):
        self.steps = []
        self.scenario_title = ""
        self.line = None
        self.executed_methods = []

    def execute(self):
        pass

    def set_line(self):
        pass

    def __str__(self):
        print("SCENARIO:")
        print("\t title: " + self.scenario_title)
        print("\t line: " + str(self.line))
        print("\t steps: ")

        for step in self.steps:
            print("\t\t" + step.keyword + step.text)

        for method in self.executed_methods:
            print('\t\t', method)

        return ''


class ScenarioOutline(Scenario):
    """ Scenario outline object """

    def __init__(self):
        self.steps = []
        self.scenario_title = ""
        self.line = None
        self.examples = []
        self.scenario_iterations = []

    def execute(self):
        """ Execute a scenario outline """
        pass

    def set_line(self):
        """ Set the line of a scenario outline """
        pass

    def add(self):
        """ Add a scenario outline """
        pass

    def remove(self):
        """ Remove a scenario outline """
        pass


class StepBdd:
    """ BDD step object """

    def __init__(self):
        self.line = None
        self.keyword = ""
        self.text = ""


class Method:
    """ Method object """

    def __init__(self):
        self.line = None
        self.method_id = ""
        self.method_name = ""
        self.class_name = ""
        self.class_path = ""
        self.abc_score = 0
        self.complexity = 0
        self.number_of_lines = 0
        self.content = ""

    def __str__(self):
        print("METHOD:")
        print("\t\t\t name: " + self.method_name)
        print("\t\t\t classe: " + self.class_name)
        print("\t\t\t path: " + self.class_path)
        return ''

    def obj_dict(self):
        """ Return a dictionary or other mapping object. """
        return self.__dict__
