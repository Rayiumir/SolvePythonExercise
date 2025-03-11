# 2. یک فایل متنی ایجاد کنید، 5 خط در آن بنویسید، آن را ذخیره کنید و چاپ کنید.

lines = ["تست\n", "تست ۱\n", "تست ۲\n", "تست ۳\n", "تست ۴\n"]

with open("file1.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)

with open("file1.txt", "r", encoding="utf-8") as file:
    print(file.read())
