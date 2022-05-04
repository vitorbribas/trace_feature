"""
    Module which declares the Project model
"""

class Project:
    """
        Project object
    """
    def __init__(self, name='', language='', repository='', methods=[]):
        self.name = name
        self.language = language
        self.repository = repository
        self.methods = methods

    def __str__(self):
        print('PROJETO:')
        print("\t name: " + self.name)
        print("\t language: " + self.language)
        print("\t Repository: " + str(self.repository))

        return ''

    def obj_dict(self):
        """ Return a dictionary or other mapping object. """
        return self.__dict__