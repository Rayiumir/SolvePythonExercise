# 9. یک فایل متنی ایجاد کنید و چند خط ساده بنویسید و تعداد خطوط موجود در فایل محاسبه کنید.

with open("text_file.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    print("تعداد خطوط:", len(lines))
