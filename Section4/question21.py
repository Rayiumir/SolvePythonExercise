# دریافت رشته از کاربر
text = input("لطفاً یک رشته وارد کنید: ")

# تبدیل رشته به لیست کلمات
words = text.split()

# ایجاد دیکشنری برای ذخیره تعداد تکرار هر کلمه
word_count = {}

# شمارش تکرار کلمات
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# چاپ کلمات تکرار شده و تعداد آن‌ها
print("کلمات تکرار شده و تعداد تکرارشان:")
for word, count in word_count.items():
    if count > 1:
        print(f"{word}: {count}")

# --------------------------
# نمونه ورودی:
# لطفاً یک رشته وارد کنید: hello world hello python world
# --------------------------

# نمونه خروجی:
# کلمات تکرار شده و تعداد تکرارشان:
# hello: 2
# world: 2
# --------------------------
