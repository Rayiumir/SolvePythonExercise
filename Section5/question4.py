# 4. اعداد اول بین دو عدد را بیابید:

def is_prime(num): # اول بودن یک عدد را بررسی می کند.
  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

def find_primes_between(start, end): # اعداد اول بین شروع و پایان را پیدا می کند.
  primes = []
  for num in range(start, end + 1):
    if is_prime(num):
      primes.append(num)
  return primes

# نمونه استفاده:
start_num = 10
end_num = 50
prime_numbers = find_primes_between(start_num, end_num)
print(f"Prime numbers between {start_num} and {end_num}: {prime_numbers}")

# Output > Prime numbers between 10 and 50: [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
