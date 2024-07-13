#!/usr/bin/python3
"""
This module defines a student by: (based on 10-student.py)
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): List of attributes to retrieve.
            Defaults to None.

        Returns:
            dict: A dictionary containing the student's attributes
            based on the attrs list or all attributes.
        """

        if attrs is None:
            return self.__dict__
        else:
            return {
                attr: self.__dict__[attr]
                for attr in attrs
                if attr in self.__dict__
            }
