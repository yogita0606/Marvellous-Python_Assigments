def main():
    num = int(input("Enter a number: "))
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print("Factorial is:", fact)

if __name__ == "__main__":
    main()
