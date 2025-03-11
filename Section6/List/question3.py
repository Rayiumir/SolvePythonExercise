# دریافت لیست از کاربر
numbers = list(map(int, input("لطفاً اعداد را با فاصله وارد کنید: ").split()))

# ایجاد لیست جدید شامل اعداد زوج
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

# نمایش لیست جدید
print("اعداد زوج لیست:", even_numbers)

# --------------------------
# نمونه ورودی:
# لطفاً اعداد را با فاصله وارد کنید: 5 12 8 3 19 2 14
# --------------------------
# نمونه خروجی:
# اعداد زوج لیست: [12, 8, 2, 14]
# --------------------------
