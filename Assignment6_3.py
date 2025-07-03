def main():
    num = int(input("Enter a number to print its multiplication table: "))

    print(f"\nMultiplication table of {num}:")
    i = 1
    while i <= 10:
        print(f"{num} x {i} = {num * i}")
        i += 1

if __name__ == "__main__":
    main()
