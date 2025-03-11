import random

# ایجاد tuple شامل مقادیر تصادفی
random_numbers = tuple(random.randint(-100, 100) for _ in range(10))

# ذخیره مقادیر مثبت
positive_numbers = tuple(num for num in random_numbers if num > 0)

# نمایش نتیجه
print("tuple شامل مقادیر تصادفی:", random_numbers)
print("مقادیر مثبت:", positive_numbers)

# نمونه خروجی:
# tuple شامل مقادیر تصادفی: (78, -12, 45, -68, 32, 0, -89, 57, -4, 23)
# مقادیر مثبت: (78, 45, 32, 57, 23)
