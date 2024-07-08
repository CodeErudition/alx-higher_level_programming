#!/usr/bin/python3
"""
This module defines a class that defines a student
by: (based on 9-student.py)
"""


class Student:
    """Represent a Student class"""
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

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary containing the student's first name,
            last name, and age.
        """
        return self.__dict__
