from geometry import Circle 

print("Partial Testing for CSS340 Lab1") 
 
c1 = Circle(3, 3, 7) 
c2 = Circle() 
 
print("First Circle Perimeter: " + str(c1.perimeter())) 
print("First Circle Area: " + str(c1.area())) 
 
c2.set_x(3) 
c2.set_y(3) 
c2.set_radius(2) 
if c2.contains_point(4, 3.7): 
    print("(4, 3.7) is within circle two") 
else: 
    print("(4, 3.7) is not within circle two") 
 
print("Moving second Circle") 
c2.set_x(3 + c2.get_x()) 
if c2.contains_point(4, 3.7): 
    print("(4, 3.7) is within circle two") 
else: 
    print("(4, 3.7) is not within circle two") 
 