#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle

'''r1 = Rectangle(1)
print(r1.width)
'''
b = Base()
print(getattr(Base, "_Base__nb_objests"))
print(b.__dict__)
r = Rectangle(1, 2, 3, 4, 5)
print(r.id)
print(str(type(r)))
print(r.__dict__)
print(r)
print(repr(b))
r1 = Rectangle(5, 9)
print(r1.id)
print(str(r1))
print(Rectangle.__str__())
