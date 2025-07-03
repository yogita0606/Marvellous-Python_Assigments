def main():
    num=int(input("Enter a number"))
        
    Calculatesquare=lambda num:num*num

    Calculatecube=lambda num:num*num*num

    print("square is:",Calculatesquare(num))
    print("cube is:",Calculatecube(num))

if __name__=="__main__":
    main()


