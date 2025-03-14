# 10. یک فایل متنی با نام کتاب ها و تعداد صفحات ایجاد کنید، سپس کتاب هایی با بیش از 300 صفحه را فیلتر کرده و به انتهای فایل اضافه کنید.

# لیستی از کتاب‌ها و تعداد صفحات
books = [
    ("کتاب اول", 250),
    ("کتاب دوم", 350),
    ("کتاب سوم", 500),
    ("کتاب چهارم", 150),
    ("کتاب پنجم", 450),
]

# ایجاد و نوشتن نام کتاب‌ها و تعداد صفحات در فایل
with open("books.txt", "w") as file:
    for book, pages in books:
        file.write(f"{book}: {pages} صفحه\n")

# فیلتر کردن کتاب‌هایی با بیش از 300 صفحه
books_over_300 = [book for book, pages in books if pages > 300]

# نوشتن کتاب‌های فیلتر شده به انتهای فایل
with open("books.txt", "a") as file:
    file.write("\nکتاب‌ های با بیش از 300 صفحه:\n")
    for book in books_over_300:
        file.write(f"{book}\n")
