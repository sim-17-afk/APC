n = int(input("Enter the value of n: "))
print("1 2 4 8 16 32 ... up to", n**2, "are:")
i=1
for _ in range(1, (n*n)+1):  
    if i>=n**2:
        break
    print(i)
    i*=2
print()
    