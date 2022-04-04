# Steven Suarez
# CSS 340
# Program 1
# 4/4/2022

import math

class Circle:

    # Constructor that verifies legitimacy of arguments before they are saved to variables.
    # If arguments are not legitimate the default values of (0, 0, 1) are used.

    def __init__(self, x: float = 0, y: float = 0, radius: float = 1):
        try:
            self._x = float(x)
        except:
            self._x = 0
        try: 
            self.y = float(y)
        except:
            self._y = 0
        
        try:
            self._radius = float(radius)
        except:
            self._radius = 1

        if radius >= 0:
            pass # radius should've already been assigned before here
        else:
            self._radius = 1 


    # Returns the x value of the origin of this circle.
    def get_x(self):
        return self._x
    
    # Sets the x-value of the origin of this circle.
    def set_x(self, new_x: float):
        try:
            self._x = float(new_x)
        except:
            self._x = 0

    # Returns the y-value of the origin of this circle.
    def get_y(self):
        return self._y

    # Sets the y-value of the origin of this circle.
    def set_y(self, new_y: float):
        try: 
            self._y = float(new_y)
        except:
            self._y = 0

    # Returns the radius of this circle. 
    def get_radius(self):
        return self._radius


    # Sets radius of this circle.
    def set_radius(self, new_radius: float):
        if new_radius >= 0:
            self._radius = new_radius
        else:
            print(str(new_radius) + " is invalid input, shutting down")
            exit()
    
    # Returns area of this circle.
    def area(self):
        return math.pi*math.pow(self._radius, 2)

    # Returns perimeter of this circle.
    def perimeter(self):
        return 2*math.pi*self._radius
    

    # Bool method that returns whether or not this circle contains a given point, using the Euclidean distance formula
    # to calculate distance from the origin. Default values are automatically assigned (0,0) upon invalid input.
    def contains_point(self, x, y):
        if math.dist([x, y], [self._x, self._y]) > self._radius:
            return False
        else:
            return True
    
