def main():
    
    num = int(input("Enter a number: "))

    if num <= 1:
     print("number is not a prime number")
    else:
      is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("number is a prime number")
    else:
        print("number is not a prime number")

if __name__=="__main__":
   main()
