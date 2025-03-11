# 1. یک فایل متنی test.txt ایجاد کنید ویک جمله ساده سلام دنیا در آن بنویسید

with open("test.txt", "w", encoding="utf-8") as file:
    file.write("سلام دنیا!")

