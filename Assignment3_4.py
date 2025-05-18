n=int(input("enter number of elements"))
list=[int(input(f"enter elements{i+1}"))for i in range(n)]
x=int(input("Enter element for search"))
print("frequency:", list.count(x))
