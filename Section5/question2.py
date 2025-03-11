# 2. شمارش ارقام زوج:

def count_even_digits(num):
  count = 0
  for digit in str(num):
    digit = int(digit)
    if digit % 2 == 0:
      count += 1
  return count

# نمونه استفاده:
number = 123456
even_count = count_even_digits(number)
print(f"Number of even digits in {number}: {even_count}")

# Output > Number of even digits in 123456: 3
