# تعریف tuple شامل سه tuple داخلی
nested_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

# استخراج مقدار خاص (مثلاً مقدار دوم از هر tuple)
first_value = nested_tuple[0][1]
second_value = nested_tuple[1][1]
third_value = nested_tuple[2][1]

# نمایش مقادیر استخراج‌شده
print("مقادیر استخراج‌شده:", first_value, second_value, third_value)

# --------------------------
# خروجی:
# مقادیر استخراج‌شده: 2 5 8
# --------------------------
