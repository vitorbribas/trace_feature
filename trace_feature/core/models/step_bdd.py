"""
    Module which declares the StepBdd model
"""

class StepBdd:
    """ BDD step object """

    def __init__(self, line=None, keyword='', text=''):
        self.line = line
        self.keyword = keyword
        self.text = text