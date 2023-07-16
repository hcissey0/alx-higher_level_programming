#!/usr/bin/python3
"""This is the base class of all other classes in this project"""


class Base:
    """This is the Base class to manage id"""

    __nb_objects = 0

    def __init__(self, id=None):
        """This is the classes initializor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of the @list_dictionaries"""
        import json
        if list_dictionaries is None:
            return "[]"
        return json.JSONEncoder().encode(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns list from a json string"""
        import json
        if json_string is None:
            return []
        return json.JSONDecoder().decode(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves the objects to a file"""
        import json
        with open(f'{cls.__name__}.json', "w") as f:
            list_dict = []
            if list_objs:
                for obj in list_objs:
                    list_dict.append(obj.to_dictionary())
            f.write(Base.to_json_string(list_dict))
