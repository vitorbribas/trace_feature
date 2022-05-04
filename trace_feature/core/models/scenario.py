"""
    Module which declares the Scenario model
"""

from abc import ABC, abstractmethod

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

  @abstractmethod
  def set_line(self):
      """
          Set line
      """