def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
prime_sum = 0
for i in range(1, 101):
    if is_prime(i):
        prime_sum += i

print("The sum of all prime numbers between 1 and 100 is:", prime_sum)
