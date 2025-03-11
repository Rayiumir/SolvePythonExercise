# 7. یک فایل متنی حاوی لیستی از اعداد ایجاد کنید، سپس لیست معکوس شده را در فایل بنویسید.

# ایجاد لیستی از اعداد
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ایجاد و نوشتن لیست اعداد در فایل
with open("numbers.txt", "w") as file:
    for number in numbers:
        file.write(f"{number}\n")

# معکوس کردن لیست اعداد
reversed_numbers = numbers[::-1]

# نوشتن لیست معکوس‌ شده در فایل
with open("numbers.txt", "a") as file:
    file.write("\nلیست معکوس‌ شده:\n")
    for number in reversed_numbers:
        file.write(f"{number}\n")
