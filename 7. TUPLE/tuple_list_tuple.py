my_tuple = ("ramen", "sushi", "tempura", "udon", "sashimi")
print("Original tuple:", my_tuple)


my_list = list(my_tuple)
print("Converted to list:", my_list)

new_tuple = tuple(my_list)
print("Converted back to tuple:", new_tuple)