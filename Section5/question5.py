# 5. مجموع اعداد فرد بین n و m:

def sum_odd_numbers_between(start, end): # مجموع اعداد فرد بین شروع و پایان را محاسبه می کند.
  total = 0
  for num in range(start, end + 1):
    if num % 2 != 0:
      total += num
  return total

# نمونه کد:

start_num = 1
end_num = 10
odd_sum = sum_odd_numbers_between(start_num, end_num)
print(f"Sum of odd numbers between {start_num} and {end_num}: {odd_sum}")

# Output > Sum of odd numbers between 1 and 10: 25


