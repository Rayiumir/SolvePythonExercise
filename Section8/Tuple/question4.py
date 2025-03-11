# ایجاد یک tuple شامل رشته‌ها
strings = ("Python", "Programming", "Tuple", "Example")

# محاسبه طول هر رشته و ذخیره در tuple جدید
lengths = tuple(len(s) for s in strings)

# نمایش نتیجه
print("طول هر رشته در tuple جدید:", lengths)

# نمونه خروجی:
# طول هر رشته در tuple جدید: (6, 11, 5, 7)
