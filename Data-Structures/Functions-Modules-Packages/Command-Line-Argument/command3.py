def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = []

print("Enter 10 numbers:")

for i in range(10):
    num = int(input())
    numbers.append(num)

prime_sum = 0

for num in numbers:
    if is_prime(num):
        prime_sum += num

print("Sum of Prime Numbers =", prime_sum)