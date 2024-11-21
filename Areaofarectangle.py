from operator import length_hint

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

area = length * width

print("The area of the rectangle is:", area)


#Area of a circle-pi*r*r

import  math

def area_of_circle(radius):
 return math.pi *radius**2
radius =5

#area = area_of_circle(radius)

print(f'The area of a circle with radius{radius}')