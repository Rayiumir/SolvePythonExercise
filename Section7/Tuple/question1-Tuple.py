# 1. اعداد زوج و فرد را در یک تاپل محاسبه کنید

def count_even_odd(data):
    even_count = sum(1 for num in data if num % 2 == 0)
    odd_count = len(data) - even_count
    return even_count, odd_count

# نمونه استفاده:
data = (1, 2, 3, 4, 5, 6)
even, odd = count_even_odd(data)
print(f"Even: {even}, Odd: {odd}")

# Output > Even: 3, Odd: 3