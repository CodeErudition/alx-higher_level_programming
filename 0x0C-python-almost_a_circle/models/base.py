#!/usr/bin/python3
"""
This module defines a class Base, which will be the base of
all other classes in this project.
"""
import json
import os
import csv


class Base():
    """
    Base class for managing 'id' attribute in future classes.

    Attributes:
        __nb_objects (int): A private class attribute that counts
        the number of instances created.

    Methods:
        __init__(self, id=None): Initializes the instance with a
        unique 'id'.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of the Base class.

        Args:
            id (int, optional): If provided, assigns the value to the
                                instance's id attribute.
                                If not provided, increments the __nb_objects
                                count and assigns the new value to id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances who inherit from Base.
        """
        f_name = cls.__name__ + ".json"
        list_dicts = (
                [obj.to_dictionary() for obj in list_objs]
                if list_objs
                else []
        )
        json_string = cls.to_json_string(list_dicts)
        with open(f_name, 'w', encoding="utf-8") as f_file:
            f_file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: The list represented by json_string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.

        Args:
            **dictionary: A dictionary of attributes to set on the instance.

        Returns:
            An instance of the class with attributes set according to
            dictionary.
        """
        if cls.__name__ == "Rectangle":
            o_dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            o_dummy = cls(1)
        else:
            raise TypeError("This class type does not exit")

        o_dummy.update(**dictionary)
        return o_dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a file.

        Returns:
            list: A list of instances.
        """
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []

        with open(filename, "r", encoding="utf-8") as r_file:
            json_string = r_file.read()

        list_dictionaries = cls.from_json_string(json_string)
        return [cls.create(**dictionary) for dictionary in list_dictionaries]

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []

        with open(filename, "r", encoding="utf-8") as r_file:
            json_string = r_file.read()

        list_dictionaries = cls.from_json_string(json_string)
        return [cls.create(**dictionary) for dictionary in list_dictionaries]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width,
                                    obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        if not os.path.exists(filename):
            return []

        with open(filename, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            list_dicts = []
            if cls.__name__ == "Rectangle":
                for row in reader:
                    dict_obj = {
                        "id": int(row[0]),
                        "width": int(row[1]),
                        "height": int(row[2]),
                        "x": int(row[3]),
                        "y": int(row[4])
                    }
                    list_dicts.append(dict_obj)
            elif cls.__name__ == "Square":
                for row in reader:
                    dict_obj = {
                        "id": int(row[0]),
                        "size": int(row[1]),
                        "x": int(row[2]),
                        "y": int(row[3])
                    }
                    list_dicts.append(dict_obj)
            return [cls.create(**d) for d in list_dicts]
