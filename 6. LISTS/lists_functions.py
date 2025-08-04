list=[]
item1=input("Enter first item:")
list.append(item1)
item2=input("Enter second item:")
list.append(item2)
item3=input("Enter third item:")
list.append(item3)
item4=input("Enter fourth item:")
list.append(item4)
item5=input("Enter fifth item:")
list.append(item5)  
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
