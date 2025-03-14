# دریافت عدد از کاربر
number = float(input("لطفاً یک عدد وارد کنید: "))

# بررسی مثبت یا منفی بودن عدد و اعمال تغییرات لازم
if number > 0:
    number += 2  # اگر عدد مثبت باشد، ۲ واحد به آن اضافه می‌شود
elif number < 0:
    number -= 2  # اگر عدد منفی باشد، ۲ واحد از آن کم می‌شود

# نمایش نتیجه
print("عدد جدید:", number)

# --------------------------
# مثال خروجی:
# اگر ورودی 5 باشد:
# عدد جدید: 7
#
# اگر ورودی -3 باشد:
# عدد جدید: -5
#
# اگر ورودی 0 باشد:
# عدد جدید: 0  (چون صفر نه مثبت است و نه منفی، تغییری نمی‌کند)
# --------------------------
