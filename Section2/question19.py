# دریافت رشته و عدد از کاربر
string = input("لطفاً یک رشته وارد کنید: ")
count = int(input("لطفاً یک عدد وارد کنید: "))

# چاپ رشته به تعداد برابر با عدد وارد شده
for _ in range(count):
    print(string)

# --------------------------
# مثال خروجی:
# اگر ورودی رشته "سلام" و عدد 3 باشد:
# سلام
# سلام
# سلام
#
# اگر ورودی رشته "دنیای پایتون" و عدد 2 باشد:
# دنیای پایتون
# دنیای پایتون
# --------------------------
