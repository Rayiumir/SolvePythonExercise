# 9. عوامل یک عدد را بیابید:

def find_factors(num): # عوامل یک عدد را پیدا می کند.
  factors = []
  for i in range(1, num + 1):
    if num % i == 0:
      factors.append(i)
  return factors

# نمونه استفاده:
number = 12
factors = find_factors(number)
print(f"Factors of {number}: {factors}")

# Output > Factors of 12: [1, 2, 3, 4, 6, 12]
