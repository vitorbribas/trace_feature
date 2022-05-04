"""
    Module which declares the Feature model
"""

class Feature:
    """
        Feature object
    """

    def __init__(self, path_name="", feature_name="", scenarios=[], language="", user_story="",
                 tags=[], line=None, background=None, project=""):
        self.path_name = path_name
        self.feature_name = feature_name
        self.scenarios = scenarios
        self.language = language
        self.user_story = user_story
        self.tags = tags
        self.line = line
        self.background = background
        self.project = project

    def __str__(self):
        return self.feature_name

    def obj_dict(self):
        """ Return a dictionary or other mapping object. """
        return self.__dict__