# # روش اول

# دریافت لیست از اعداد
numbers = list(map(int, input("لطفاً اعداد را با فاصله وارد کنید: ").split()))

# محاسبه مجموع اعداد در ایندکس‌های زوج
even_index_sum = sum(numbers[i] for i in range(0, len(numbers), 2)) # استفاده از متود sum برای جمع اعداد به دست امده

# نمایش مجموع
print("مجموع اعداد در ایندکس‌های زوج:", even_index_sum)


# # روش دوم

# دریافت لیست از اعداد
numbers = list(map(int, input("لطفاً اعداد را با فاصله وارد کنید: ").split()))

# متغیر برای ذخیره مجموع
even_index_sum = 0

# استفاده از for برای پیدا کردن اعداد در ایندکس‌های زوج و جمع کردن آنها
for i in range(0, len(numbers), 2):
    even_index_sum += numbers[i]

# نمایش مجموع
print("مجموع اعداد در ایندکس‌های زوج:", even_index_sum)


# --------------------------
# نمونه ورودی:
# لطفاً اعداد را با فاصله وارد کنید: 1 2 3 4 5 6 7 8 9
# --------------------------
# نمونه خروجی:
# مجموع اعداد در ایندکس‌های زوج: 25  (1 + 3 + 5 + 7 + 9)
# --------------------------
