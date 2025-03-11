def print_border(width, height):
    # چاپ خط اول حاشیه
    print("*" * width)

    # چاپ حاشیه با فضای خالی در وسط
    for _ in range(height - 2):
        print("*" + " " * (width - 2) + "*")

    # چاپ خط آخر حاشیه
    print("*" * width)


def print_centered_text(width, height, text):
    # پیدا کردن موقعیت متن برای نمایش در وسط
    space_before = (width - len(text) - 2) // 2
    space_after = width - len(text) - space_before - 2

    # تعداد خطوط برای حاشیه بالایی و پایینی
    space_between = height - 3  # 1 خط حاشیه بالایی، 1 خط حاوی متن و 1 خط حاشیه پایینی

    # چاپ حاشیه بالایی
    print("*" * width)

    # چاپ خطوط خالی بین حاشیه بالا و متن
    for _ in range(space_between // 2):
        print("*" + " " * (width - 2) + "*")

    # چاپ خط حاوی متن در وسط
    print("*" + " " * space_before + text + " " * space_after + "*")

    # چاپ خطوط خالی بین متن و حاشیه پایینی
    for _ in range(space_between - space_between // 2 - 1):
        print("*" + " " * (width - 2) + "*")

    # چاپ حاشیه پایینی
    print("*" * width)


# ورودی از کاربر
text = input("متن دلخواه خود را وارد کنید: ")
width = 50  # عرض حاشیه
height = 10  # ارتفاع حاشیه

# نمایش متن در وسط حاشیه
print_centered_text(width, height, text)

# --------------------------
# نمونه ورودی:
# متن دلخواه خود را وارد کنید: خوش آمدید به دنیای پایتون!
# --------------------------

# نمونه خروجی:
# **************************************************
# *                                                *
# *                                                *
# *                                                *
# *                                                *
# *             خوش آمدید به دنیای پایتون!         *
# *                                                *
# *                                                *
# *                                                *
# *                                                *
# **************************************************
# --------------------------
