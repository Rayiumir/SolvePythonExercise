# دریافت دو عدد از کاربر و تبدیل آن‌ها به عدد صحیح
num1 = int(input("لطفاً عدد اول را وارد کنید: "))
num2 = int(input("لطفاً عدد دوم را وارد کنید: "))

# محاسبه مجموع دو عدد
sum_numbers = num1 + num2

# بررسی اینکه آیا مجموع بزرگتر از 100 است یا نه
if sum_numbers > 100:
    print("مجموع دو عدد بزرگتر از ۱۰۰ است.")
else:
    print("مجموع دو عدد بزرگتر از ۱۰۰ نیست.")

# --------------------------
# مثال خروجی:
# اگر ورودی‌ها 60 و 50 باشند:
# مجموع دو عدد بزرگتر از ۱۰۰ است.
#
# اگر ورودی‌ها 30 و 40 باشند:
#
