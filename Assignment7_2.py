def main():
   
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))


    doubled = list(map(lambda x: x * 2, numbers))


    print("Doubled values:", doubled)


    


if __name__=="__main__":
    main()