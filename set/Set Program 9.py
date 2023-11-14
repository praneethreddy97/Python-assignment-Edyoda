
#9.Python Set – Pairs of complete strings in two sets

set1={"apple","mango","Banana"}
set2={"apple","grape","cherry","strawberry"}

pairs= set()

for string1 in set1:
    for string2 in set2:
        if string1 == string2:
            pairs.add((string1,string2))

pairs_list = list(pairs)
for pair in pairs_list:
    print(f"Complete string pair: {pair}")
