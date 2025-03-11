import csv

# نام فایل ورودی و خروجی
input_filename = "data.csv"
output_filename = "cleaned_data.csv"

cleaned_data = []

# خواندن داده‌ها از فایل CSV ورودی
with open(input_filename, mode='r', encoding='utf-8', newline='') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        # اصلاح ستون "Name": اگر خالی بود، مقدار پیش‌فرض "Unknown" در نظر گرفته می‌شود.
        if "Name" in row:
            if row["Name"].strip() == "":
                row["Name"] = "Unknown"
        else:
            row["Name"] = "Unknown"

        # اصلاح ستون "Age": تلاش می‌شود به عدد تبدیل شود؛ در صورت عدم موفقیت یا مقدار منفی، مقدار پیش‌فرض "0" در نظر گرفته می‌شود.
        if "Age" in row:
            try:
                age = int(row["Age"])
                if age < 0:  # سن منفی مجاز نیست
                    age = 0
                row["Age"] = str(age)
            except ValueError:
                row["Age"] = "0"
        else:
            row["Age"] = "0"

        # اصلاح ستون "Grade": اگر خالی بود، مقدار پیش‌فرض "N/A" در نظر گرفته می‌شود.
        if "Grade" in row:
            if row["Grade"].strip() == "":
                row["Grade"] = "N/A"
        else:
            row["Grade"] = "N/A"

        # اضافه کردن ردیف اصلاح‌شده به لیست
        cleaned_data.append(row)

# ذخیره داده‌های اصلاح‌شده در فایل CSV جدید
with open(output_filename, mode='w', encoding='utf-8', newline='') as outfile:
    fieldnames = ["Name", "Age", "Grade"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(cleaned_data)

# نمایش داده‌های اصلاح‌شده در کنسول (ردیف به ردیف)
print("داده‌های اصلاح‌شده:")
for row in cleaned_data:
    print(row)

print(f"\nداده‌های پاک‌سازی شده در فایل '{output_filename}' ذخیره شدند.")

# نمونه ورودی (محتوای فایل data.csv):
# Name,Age,Grade
# Ali,15,10
# ,20,9
# Sara,abc,8
# Reza,,11
# Fatima,17,
# نمونه خروجی (در کنسول):
# داده‌های اصلاح‌شده:
# {'Name': 'Ali', 'Age': '15', 'Grade': '10'}
# {'Name': 'Unknown', 'Age': '20', 'Grade': '9'}
# {'Name': 'Sara', 'Age': '0', 'Grade': '8'}
# {'Name': 'Reza', 'Age': '0', 'Grade': '11'}
# {'Name': 'Fatima', 'Age': '17', 'Grade': 'N/A'}
#
# داده‌های پاک‌سازی شده در فایل 'cleaned_data.csv' ذخیره شدند.
