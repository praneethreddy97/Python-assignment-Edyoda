#10.Python program to convert Set into Tuple and Tuple into Set

set1={1,2,3,4,5}
tuple1=tuple(set1)

print("Set converted to a tuple", tuple1)

tuple2={1,2,3,4,5}
set2=set(tuple2)

print("tuple converted to a set", set2)
