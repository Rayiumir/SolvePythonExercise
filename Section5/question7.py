# 7. عدد اول بعد از n را پیدا کنید:

def is_prime(num): # اولین عدد اول بزرگتر از n را پیدا می کند.
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def next_prime(n):
    """Finds the next prime number after n."""
    number = n + 1
    while True:
        if is_prime(number):
            return number
        number += 1

# نمونه استفاده:
n = 17
next_prime_number = next_prime(n)
print(f"The next prime number after {n} is {next_prime_number}")

# Output > The next prime number after 17 is 19

