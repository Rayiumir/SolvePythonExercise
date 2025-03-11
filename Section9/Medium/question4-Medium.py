# 4. یک فایل متنی ایجحاد و با استفاده از برنامه باز کرده و محتویات آن به صورت خط به خط در یک لیست ذخیره کنید.

with open("reverse_text.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

with open("reversed_output.txt", "w", encoding="utf-8") as file:
    for line in lines:
        file.write(line[::-1] + "\n")
