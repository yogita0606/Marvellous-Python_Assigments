

from MarvellousNum import checkprime

def listprime():
    n = int(input("Enter how many numbers you want to input: "))
    numbers = []
    
    for i in range(n):
        num = int(input(f"Enter number {i+1}: "))
        numbers.append(num)

    prime_sum = 0
    for num in numbers:
        if checkprime(num):
            prime_sum += num

    print("Sum of prime numbers in the list:", prime_sum)

def main():
    listprime()
    print("addition of prime numbers")

if __name__=="__main__":
    main()



