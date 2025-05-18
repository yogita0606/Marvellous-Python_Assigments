n = int(input("Enter a number: "))
sum_of_factors = 0
for i in range(1, n):
    if n % i == 0:
        sum_of_factors += i
print("Output:", sum_of_factors)
