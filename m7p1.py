#Luan Nguyen

#June 8th 2023

#Write a function areaOfCircle(r) which returns the area of a circle of radius r
import math
def areaOfCircle(r):
    area = math.pi * (r ** 2)
    return area

r = float(input("Enter the radius: "))
print ("The radius is: R = ", r);
area_of_circle =areaOfCircle(r)
print ("Area of a circle: A = ", area_of_circle);