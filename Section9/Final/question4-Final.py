# 4. یک فایل متنی حاوی نام روزهای هفته ایجاد کنید. سپس روزها را با بیش از 5 حرف استخراج کرده و در یک فایل جدید ذخیره کنید.

# لیستی از روزهای هفته
days_of_week = [
    "یکشنبه",
    "دوشنبه",
    "سه‌شنبه",
    "چهارشنبه",
    "پنج‌شنبه",
    "جمعه",
    "شنبه"
]

# ایجاد و نوشتن روزهای هفته در فایل
with open("days_of_week.txt", "w") as file:
    for day in days_of_week:
        file.write(day + "\n")

# خواندن روزهای هفته از فایل
with open("days_of_week.txt", "r") as file:
    days = file.readlines()

# استخراج روزهایی که بیشتر از 5 حرف دارند
days_more_than_5 = [day.strip() for day in days if len(day.strip()) > 5]

# ذخیره روزهایی که بیشتر از 5 حرف دارند در فایل جدید
with open("days_more_than_5.txt", "w") as file:
    for day in days_more_than_5:
        file.write(day + "\n")

# چاپ روزهایی که بیشتر از 5 حرف دارند
print("روزهایی که بیش از 5 حرف دارند:")
for day in days_more_than_5:
    print(day)

