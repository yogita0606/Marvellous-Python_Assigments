def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes(numbers):
    return list(filter(is_prime, numbers))


nums = list(map(int, input("Enter numbers separated by space: ").split()))
prime_list = get_primes(nums)

print("Prime numbers are:", prime_list)
