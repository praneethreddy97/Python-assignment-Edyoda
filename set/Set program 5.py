#5.Python – Check if two lists have at-least one element common

a={1,2,3,4,5}

b={5,6,7,8,9}

if a.intersection(b):
    print("it has atleast one common element")
else:
    print("No common element")
