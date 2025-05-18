n = int(input("Enter a number: "))
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Output: It is not Prime Number")
            break
    else:
        print("Output: It is Prime Number")
else:
    print("Output: It is not Prime Number")