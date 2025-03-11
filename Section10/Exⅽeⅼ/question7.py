from openpyxl import Workbook

# ایجاد یک Workbook جدید
wb = Workbook()
ws = wb.active
ws.title = "لیست کتاب‌ها"

# افزودن عنوان ستون‌ها
ws.append(["نام کتاب", "تعداد صفحات", "بیش از ۳۰۰ صفحه؟"])

# لیست کتاب‌ها و تعداد صفحات آن‌ها
books = [
    ("کتاب اول", 250),
    ("کتاب دوم", 320),
    ("کتاب سوم", 150),
    ("کتاب چهارم", 450),
    ("کتاب پنجم", 300),
    ("کتاب ششم", 500)
]

# افزودن اطلاعات به فایل اکسل
for book, pages in books:
    more_than_300 = "✔" if pages > 300 else "✘"
    ws.append([book, pages, more_than_300])

# ذخیره فایل اکسل
wb.save("books_with_pages.xlsx")

print("فایل اکسل با موفقیت ایجاد شد.")
