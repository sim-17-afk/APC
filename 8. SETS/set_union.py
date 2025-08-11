set_one=set()
print("Empty Set:", set_one)
set_one.add("Simoni")
print("Set after adding an element:", set_one)
set_one.add("Ishaan")
print("Set after adding another element:", set_one)
set_one.add("Vedant")
print("Set after adding a third element:", set_one)   

set_two=set()
print("Empty Set:", set_two)
set_two.add("Simoni")
print("Set after adding an element:", set_two)
set_two.add("Diya")
print("Set after adding another element:", set_two)
set_two.add("Vedant")
print("Set after adding a third element:", set_two)


set_union=set_one.union(set_two)
print("Union of two sets:", set_union)

set_intersection=set_one.intersection(set_two)
print("Intersection of two sets:", set_intersection)

set_difference=set_one.difference(set_two)
print("Difference of two sets (set_one - set_two):", set_difference)