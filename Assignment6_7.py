def main():
    num1=int(input("Enter a number"))
    num2=int(input("Enter a number"))
    num3=int(input("Enter a number"))
    num4=int(input("Enter a number"))
    num5=int(input("Enter a number"))

    largest = num1

    if num2 > largest:
       largest = num2
    if num3 > largest:
       largest = num3
    if num4 > largest:
       largest = num4
    if num5 > largest:
       largest = num5

    print("largest number is :",largest)


if __name__=="__main__":
    main()