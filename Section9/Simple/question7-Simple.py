# 7. یک فایل متنی بسازید و متن ساده در آن بنویسید و سپس این فایل باز کرده و تعداد کلمات موجود در آن محاسبه کنید.

text = """این یک متن نمونه است.
ما در حال تمرین کار با فایل ها هستیم.
پایتون زبان جالبی است.
"""

with open("text_file.txt", "w", encoding="utf-8") as file:
    file.write(text)

with open("text_file.txt", "r", encoding="utf-8") as file:
    content = file.read()
    words = content.split()
    print("تعداد کلمات:", len(words))
