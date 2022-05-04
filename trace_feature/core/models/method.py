"""
    Module which declares the Method model
"""

class Method:
    """ Method object """

    def __init__(self, line=None, method_id="", method_name="", class_name="", class_path="",
                 abc_score=0, complexity=0, number_of_lines=0, content=""):
        self.line = line
        self.method_id = method_id
        self.method_name = method_name
        self.class_name = class_name
        self.class_path = class_path
        self.abc_score = abc_score
        self.complexity = complexity
        self.number_of_lines = number_of_lines
        self.content = content

    def __str__(self):
        print("METHOD:")
        print("\t\t\t name: " + self.method_name)
        print("\t\t\t classe: " + self.class_name)
        print("\t\t\t path: " + self.class_path)
        return ''

    def obj_dict(self):
        """ Return a dictionary or other mapping object. """
        return self.__dict__