#4.Python Program to find Area and Perimeter of Square and Rectangle

length=float(input("Enter length or side"))

width=float(input("enter width"))

area_square= length**2
perimeter_square= 4* length

print(f"area of square is {area_square}\n Perimeter of square is {perimeter_square}\n")

area_Rectangle= length*width
perimeter_Rectangle= 2*(length + width)

print(f"area of Rectangle is {area_Rectangle}\n Perimeter of Rectangle is {perimeter_Rectangle}\n")
