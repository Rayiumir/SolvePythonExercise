# 5. یک فایل متنی حاوی یک جمله ایجاد کنید، سپس تکرار هر کلمه در جمله را محاسبه کرده و نتایج را در فایل ذخیره کنید.

from collections import Counter

# یک فایل بسازید و یک جمله بنویسید
sentence = "This is a sample sentence where words repeat words."

with open("sentence.txt", "w") as file:
    file.write(sentence)

# جمله را از روی فایل بخوانید
with open("sentence.txt", "r") as file:
    sentence = file.read()

# جمله را به کلمات تقسیم کنید و تکرار هر کلمه را محاسبه می کند
words = sentence.split()
word_count = Counter(words)

# خروجی
with open("sentence.txt", "a") as file:
    file.write("\nWord frequencies:\n")
    for word, count in word_count.items():
        file.write(f"{word}: {count} repeat\n")


