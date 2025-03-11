import random

# ایجاد لیستی از 10 عدد تصادفی بین 1 تا 100
random_numbers = [random.randint(1, 100) for _ in range(10)]

# فیلتر کردن اعداد فرد
odd_numbers = [num for num in random_numbers if num % 2 != 0]

# نمایش لیست‌ها
print("لیست اعداد تصادفی:", random_numbers)
print("لیست اعداد فرد:", odd_numbers)

# نمونه خروجی:
# لیست اعداد تصادفی: [42, 17, 58, 33, 91, 76, 20, 15, 63, 84]
# لیست اعداد فرد: [17, 33, 91, 15, 63]
