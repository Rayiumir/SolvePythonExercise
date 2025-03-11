# 1. یک ست از اعداد ایجاد کنید و مجموع اعداد زوج و فرد را جداگانه محاسبه کنید

numbers = {1, 2, 3, 4, 5, 6}
even_sum = sum(x for x in numbers if x % 2 == 0)
odd_sum = sum(x for x in numbers if x % 2 != 0)

print(f"Even sum: {even_sum}, Odd sum: {odd_sum}")

# Output > Even sum: 12, Odd sum: 9