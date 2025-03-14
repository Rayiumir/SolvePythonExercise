# دریافت لیست از کاربر
numbers = list(map(int, input("لطفاً اعداد را با فاصله وارد کنید: ").split()))

# پیدا کردن کوچک‌ترین و بزرگ‌ترین عدد
min_num = numbers[0]
max_num = numbers[0]

for num in numbers:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num

# نمایش نتایج
print("کوچک‌ترین عدد لیست:", min_num)
print("بزرگ‌ترین عدد لیست:", max_num)

# --------------------------
# نمونه ورودی:
# لطفاً اعداد را با فاصله وارد کنید: 5 12 8 3 19 1
# --------------------------
# نمونه خروجی:
# کوچک‌ترین عدد لیست: 1
# بزرگ‌ترین عدد لیست: 19
# --------------------------
