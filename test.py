from geometry import Circle 
print("Partial Testing for CSS340 Lab1") 
 
c1 = Circle(1, 1, 1) 
c2 = Circle() 
 
print("First Circle Perimeter: " + str(c1.perimeter())) 
print("First Circle Area: " + str(c1.area())) 
 
c2.set_x(2) 
c2.set_y(2) 
c2.set_radius(1) 
if c2.contains_point(3, 3): 
    print("(3, 3) is within circle two") 
else: 
    print("(3, 3) is not within circle two") 
 
print("Moving second Circle") 
c2.set_x(1 + c2.get_x())
c2.set_y(1 + c2.get_y())
if c2.contains_point(3, 3): 
    print("(3, 3) is within circle two") 
else: 
    print("(3, 3) is not within circle two") 
