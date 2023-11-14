#Python Program for Program to find area of a circle
import math
def cirlce_area(radius):
    if radius > 0:
        area= math.pi * (radius**2)
        return area
    else:
        print("Radius cannot be negative")

radius=float(input("Enter a radius: "))

result= cirlce_area(radius)

print(f"area of circle is {result:.2f}")
