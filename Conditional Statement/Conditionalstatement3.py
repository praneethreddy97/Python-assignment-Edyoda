"""Python program For Checking Leap Year or Not"""

checkleap= int(input("enter a year:"))

if(checkleap % 4 == 0 and checkleap % 100!= 0) or (checkleap % 400 == 0):
    print("it is leap year")
else:
    print("it is not leap year")
