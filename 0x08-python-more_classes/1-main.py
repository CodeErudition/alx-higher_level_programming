#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(-2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = -3
print(my_rectangle.__dict__)
try:
    myrectangle = Rectangle(2, -3) 
except Exception as e:
    print("[{}] {}".format(type(e).__name__, e))
try:
    myrectangle = Rectangle(-2, 3)
except Exception as e:
    print("[{}] {}".format(type(e).__name__, e))
