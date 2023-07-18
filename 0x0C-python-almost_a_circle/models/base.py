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
        if json_string:
            return json.JSONDecoder().decode(json_string)
        else:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves the objects to a file"""
        import json
        with open(f'{cls.__name__}.json', "w") as f:
            list_dict = []
            if list_objs:
                for obj in list_objs:
                    list_dict.append(obj.to_dictionary())
            f.write(cls.to_json_string(list_dict))

    @classmethod
    def create(cls, **dictionary):
        """This method creates a new instace of the calling class"""
        temp = None
        if cls.__name__ == "Rectangle":
            temp = cls(1, 1)
        elif cls.__name__ == "Square":
            temp = cls(1)
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """Loads a list of instances from a file"""
        filename = cls.__name__ + ".json"
        try:
            res = []
            with open(filename, "r") as f:
                list_dict = cls.from_json_string(f.read())
                for dic in list_dict:
                    res.append(cls.create(**dic))
            return res
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves the object in the list to a csv file"""
        import csv
        filename = cls.__name__ + ".csv"
        fieldnames = ["id", "width", "height", "size", "x", "y"]
        with open(filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            if list_objs:
                for obj in list_objs:
                    dict_row = obj.to_dictionary()
                    if cls.__name__ == "Rectangle":
                        dict_row.pop('size', None)
                    elif cls.__name__ == "Square":
                        dict_row.pop("width", None)
                        dict_row.pop("height", None)
                    writer.writerow(dict_row)

    @classmethod
    def load_from_file_csv(cls):
        """Loads objects from a file"""
        import csv
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as f:
                reader = csv.DictReader(f)
                list_objs = []
                for row in reader:
                    dic = {k: int(v) for k, v in row.items() if v.isdigit()}
                    obj = cls.create(**dic)
                    list_objs.append(obj)
                return list_objs
        except Exception:
            return []
