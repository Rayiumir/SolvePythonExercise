# 3. یک فایل متنی ایجاد کنید و 10 عدد تصادفی را در آن بنویسید، سپس محتویات آن را با استفاده از یک برنامه نمایش دهید.

import random

numbers = [str(random.randint(1, 100)) + "\n" for _ in range(10)]

with open("numbers.txt", "w", encoding="utf-8") as file:
    file.writelines(numbers)

with open("numbers.txt", "r", encoding="utf-8") as file:
    print(file.read())