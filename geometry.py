import math
from re import X
from tkinter import Y

class Circle:

    def __init__(self, _x: float = 0, _y: float = 0, _radius: float = 1):
        self._x = _x
        self._y = _y
        self._radius = _radius

    def get_x(self):
        return self._x
    
    def set_x(self, new_x: float):
       self._x = new_x


    def get_x(self):
        return self._y

    def set_y(self, new_y: float):
       self._y = new_y

    def get_y(self):
        return self._y
        
    def get_radius(self):
        return self._radius

    def set_radius(self, new_radius: float):
        if new_radius >= 0:
            self._radius = new_radius
        else:
            print(new_radius + " is invalid, shutting down")
            exit()
    
    def area(self):
        return math.pi*math.pow(self._radius, 2)

    def perimeter(self):
        return 2*math.pi*self._radius
    
    def contains_point(self, x, y):
        
        if x > (self._x + self._radius) or x < (self._x - self._radius):
            return False
        if y > (self._y + self._radius) or y < (self._y - self._radius):
            return False
        return True
        
