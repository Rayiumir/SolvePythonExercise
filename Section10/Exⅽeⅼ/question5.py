from openpyxl import Workbook

# ایجاد یک شیء Workbook
wb = Workbook()

# انتخاب برگه فعال
ws = wb.active
ws.title = "محصولات و قیمت ها"

# وارد کردن نام محصولات و قیمت های آنها
products = [
    ("محصول 1", 100000),
    ("محصول 2", 200000),
    ("محصول 3", 300000),
    ("محصول 4", 400000),
    ("محصول 5", 500000)
]

# وارد کردن داده‌ها به اکسل
ws.append(["نام محصول", "قیمت", "قیمت پس از تخفیف ۲۰٪"])  # عنوان ستون‌ها
for product in products:
    ws.append(product)

# اضافه کردن فرمول برای محاسبه قیمت پس از تخفیف ۲۰٪
for i in range(2, len(products) + 2):
    price_cell = f"B{i}"  # سلول قیمت
    discount_formula = f"={price_cell}*0.8"  # فرمول برای اعمال تخفیف ۲۰٪
    ws[f"C{i}"] = discount_formula

# ذخیره فایل اکسل
wb.save("products_with_discount.xlsx")

# پیامی که نشان دهد فایل ذخیره شده است
print("فایل اکسل با موفقیت ذخیره شد.")
