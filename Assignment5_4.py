def main():
    a=int(input("Enter a first number"))
    b=int(input("Enter a second number"))
    c=int(input("Enter a third number"))

    if a>b:
        if a>c:
            print("Largest number is:",a)
        else:
            print("Largest Number is:",c)
    else:

        if b>c:
            print("Largest number is:",b)

        else:
            print("Largest number is :",c)

if __name__=="__main__":
    main()

        