a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

if a > b:
    print(f"The largest number is {a}.")
elif b > a:
    print(f"The largest number is {b}.")
else:
    print("Both numbers are equal.")