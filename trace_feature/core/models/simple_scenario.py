"""
    Module which declares the SimpleScenario model
"""

from abc import ABC, abstractmethod
from trace_feature.core.models.scenario import Scenario

class SimpleScenario(Scenario):
    """ Simple scenario object """

    def __init__(self, steps=[], scenario_title="", line=None, executed_methods=[]):
        super().__init__()
        self.steps = steps
        self.scenario_title = scenario_title
        self.line = line
        self.executed_methods = executed_methods

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