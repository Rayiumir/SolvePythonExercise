# 8. یک فایل متنی ایجاد کنید و برای هر خط از کلمات آن ابتدا تعداد کاراکتر ها و تعداد کلمات موجود در آن چاپ کند.

with open("text_file.txt", "r", encoding="utf-8") as file:
    content = file.read()

char_count = len(content)
word_count = len(content.split())

print(f"تعداد کاراکترها: {char_count}")
print(f"تعداد کلمات: {word_count}")
