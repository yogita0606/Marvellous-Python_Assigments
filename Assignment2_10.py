def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

# Input
num = int(input("Enter a number: "))
print("Output:", sum_of_digits(num))
