# دریافت سن از کاربر و تبدیل آن به عدد صحیح
age = int(input("لطفاً سن خود را وارد کنید: "))

# بررسی سن و نمایش پیام مناسب
if age > 18:
    print("بالغ")
else:
    print("نابالغ")

# --------------------------
# مثال خروجی:
# اگر ورودی 20 باشد:
# بالغ
#
# اگر ورودی 15 باشد:
# نابالغ
# --------------------------
