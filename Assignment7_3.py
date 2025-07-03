def main():
    numbers=list(map(int,input("Enter a number separated by space:").split()))

    evennumber=list(filter(lambda num:num%2==0,numbers))

    print("even number is:",evennumber)

if __name__=="__main__":
    main()