# 6. شمارش ارقام فرد:

def count_odd_digits(num): # تعداد ارقام فرد را در یک عدد می شمارد.
  count = 0
  for digit in str(num):
    digit = int(digit)
    if digit % 2 != 0:
      count += 1
  return count

# Example usage:
number = 1234567
odd_count = count_odd_digits(number)
print(f"Number of odd digits in {number}: {odd_count}")

# Output > Number of odd digits in 1234567: 4
