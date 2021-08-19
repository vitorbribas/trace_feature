"""
    Base execution for ABC method
"""

from abc import ABC, abstractmethod


class BaseExecution(ABC):
    """
        BaseExecution class
    """

    @abstractmethod
    def execute(self, path):
        """
            BaseExecution execute self
        """

    # this method will execute only a specific feature
    @abstractmethod
    def execute_feature(self, path, filename):
        """
            BaseExecution execute for specific feature
        """

    # this method will execute a specific scenario into a specific feature
    # filename: refer to the .feature file
    # scenario_ref: refer to the line or the name of a specific scenario
    @abstractmethod
    def execute_scenario(self, filename, scenario_ref):
        """
            BaseExecution execute for specific scenario into a specific feature
        """
