# 3. یک فایل متنی حاوی نام کشورها و پایتخت آنها ایجاد کنید. سپس نام پایتخت ها را بر اساس حروف الفبا مرتب کنید و در فایل ذخیره کنید.

# لیستی از کشورهای و پایتخت‌ها
countries_and_capitals = [
    ("ایران", "تهران"),
    ("آلمان", "برلین"),
    ("فرانسه", "پاریس"),
    ("ژاپن", "توکیو"),
    ("بریتانیا", "لندن"),
    ("ایالات متحده آمریکا", "واشنگتن دی سی"),
    ("روسیه", "مسکو"),
    ("چین", "پکن"),
]

# ایجاد و نوشتن نام کشورهای و پایتخت‌ها در فایل
with open("countries_and_capitals.txt", "w") as file:
    for country, capital in countries_and_capitals:
        file.write(f"{country}: {capital}\n")

# خواندن نام کشورهای و پایتخت‌ها از فایل
with open("countries_and_capitals.txt", "r") as file:
    lines = file.readlines()

# استخراج پایتخت‌ها از هر خط
capital_list = [line.split(": ")[1].strip() for line in lines]

# مرتب کردن پایتخت‌ها بر اساس حروف الفبا
sorted_capitals = sorted(capital_list)

# ذخیره پایتخت‌های مرتب شده در فایل جدید
with open("sorted_capitals.txt", "w") as file:
    file.write("پایتخت‌های مرتب شده بر اساس حروف الفبا:\n")
    for capital in sorted_capitals:
        file.write(f"{capital}\n")

# چاپ پایتخت‌های مرتب شده
print("پایتخت‌های مرتب شده بر اساس حروف الفبا:")
for capital in sorted_capitals:
    print(capital)
