# 5. یک فایل متنی ایجاد کنید و هر هط آن را با یک عدد تصادفی به انتهای آن اضافه کنید.

with open("reverse_text.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

with open("reverse_text.txt", "w", encoding="utf-8") as file:
    for index, line in enumerate(lines, start=1):
        file.write(f"{index}. {line}")
