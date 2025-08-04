size=input("Enter the size of the list:")
list=[]
for i in range(int(size)):
    item=input(f"Enter item {i+1}:")
    list.append(item)

print("The list is:", list)


rem=input("Enter an item to remove from the list:")
list.remove(rem)
print("The list after removing", rem, "is:", list)

add=input("Enter an item to add to the list:")
list.append(add)
print("The list after adding", add, "is:", list)

sor=input("Enter 'asc' to sort in ascending order:")
list.sort()
print("The list in ascending order is:", list)

cou=input("Enter an item to count in the list:")
count=list.count(cou)
