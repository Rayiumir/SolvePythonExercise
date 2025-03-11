# 7. یک فایل متنی حاوی چندین رشته ایجاد کنید. سپس، از یک برنامه استفاده کنید و برای تمام رشته هایی که بیش از 10 کاراکتر هستند را چاپ کنید.

# لیستی از رشته‌ها
strings = [
    "این یک جمله کوتاه است",
    "این جمله‌ای با بیش از ده کاراکتر است",
    "Python programming",
    "یک جمله بلند دیگر با تعداد کاراکتر زیاد",
    "کوتاه"
]

# ایجاد فایل و نوشتن رشته‌ها در آن
with open("strings.txt", "w") as file:
    for string in strings:
        file.write(string + "\n")

# خواندن داده‌ها از فایل
with open("strings.txt", "r") as file:
    lines = file.readlines()

# چاپ رشته‌هایی که بیشتر از 10 کاراکتر دارند
print("رشته‌هایی که بیش از 10 کاراکتر دارند:")
for line in lines:
    if len(line.strip()) > 10:
        print(line.strip())
