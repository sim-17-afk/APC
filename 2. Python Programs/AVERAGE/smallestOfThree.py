a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

if a < b and a < c:
    print(f"The smallest number is {a}.")
elif b < a and b < c:
    print(f"The smallest number is {b}.")
elif c < a and c < b:
    print(f"The smallest number is {c}.")
else:
    print("Two numbers are equal.")