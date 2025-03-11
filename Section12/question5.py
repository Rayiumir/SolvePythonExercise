import csv  # ایمپورت کتابخانه CSV

# مسیر فایل CSV (فرض می‌کنیم فایل students.csv در همان مسیر قرار دارد)
filename = "students.csv"

# باز کردن فایل CSV برای خواندن
with open(filename, mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)  # ایجاد شیء reader برای خواندن فایل CSV
    # خواندن و چاپ هر ردیف به صورت جداگانه
    for row in csv_reader:
        print(row)

# نمونه ورودی (محتوای فایل students.csv):
# Name,Age,Grade
# Ali,15,10
# Sara,14,9
# Reza,16,11
#
# نمونه خروجی:
# ['Name', 'Age', 'Grade']
# ['Ali', '15', '10']
# ['Sara', '14', '9']
# ['Reza', '16', '11']
