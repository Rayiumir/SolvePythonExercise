# # روش اول

# تعریف یک tuple شامل اعداد

numbers = (12, 5, 8, 20, 3, 15)

# یافتن کوچک‌ترین و بزرگ‌ترین مقدار
min_value = min(numbers)
max_value = max(numbers)

# نمایش نتایج
print("کوچک‌ترین مقدار:", min_value)
print("بزرگ‌ترین مقدار:", max_value)

# # روش دوم

# تعریف یک tuple شامل اعداد
numbers = (12, 5, 8, 20, 3, 15)

# مقدار اولیه برای کوچک‌ترین و بزرگ‌ترین عدد
min_value = numbers[0]
max_value = numbers[0]

# پیمایش tuple برای یافتن کمترین و بیشترین مقدار
for num in numbers:
    if num < min_value:
        min_value = num
    if num > max_value:
        max_value = num

# نمایش نتایج
print("کوچک‌ترین مقدار:", min_value)
print("بزرگ‌ترین مقدار:", max_value)

# --------------------------
# خروجی:
# کوچک‌ترین مقدار: 3
# بزرگ‌ترین مقدار: 20
# --------------------------
