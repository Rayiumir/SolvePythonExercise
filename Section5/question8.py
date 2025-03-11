# 8. معکوس کردن لیست اعداد:

def reverse_list(lst):
  return lst[::-1]

# نمونه استفاده:
numbers = [1, 2, 3, 4, 5]
reversed_numbers = reverse_list(numbers)
print(f"Reversed list: {reversed_numbers}")

# Output > Reversed list: [5, 4, 3, 2, 1]