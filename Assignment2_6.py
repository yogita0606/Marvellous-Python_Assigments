n=int(input("Enter a Number:"))
for i in range(n):
    for j in range(n-i):
        print("*",end="")
    print()