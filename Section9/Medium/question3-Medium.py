# 3. یک فایل متنی ایجاد کنید، محتوای آن را به صورت معکوس چاپ کنید.

content = """این یک متن نمونه است.
ما در حال یادگیری پایتون هستیم.
فایل‌ها بسیار مهم هستند.
"""

with open("reverse_text.txt", "w", encoding="utf-8") as file:
    file.write(content)

with open("reverse_text.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in reversed(lines):
        print(line.strip())
