import csv
from collections import defaultdict

# نام فایل CSV که شامل اطلاعات مالی شخصی است
csv_filename = "personal_finance.csv"

# متغیرها برای ذخیره اطلاعات مالی
income = 0
expenses = defaultdict(float)
savings = 0
budget = {}

# خواندن فایل CSV
with open(csv_filename, newline='', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # خواندن هدر (نام ستون‌ها)

    for row in reader:
        category = row[0]  # نوع (درآمد، هزینه، پس‌انداز)
        subcategory = row[1]  # نام دسته‌بندی
        amount = float(row[2])  # مقدار پول
        type_ = row[3]  # نوع تراکنش (درآمد/هزینه/پس‌انداز)
        allocated_budget = float(row[4]) if row[4] else 0  # بودجه تعیین‌شده (اختیاری)

        if type_ == "درآمد":
            income += amount
        elif type_ == "هزینه":
            expenses[subcategory] += amount
            budget[subcategory] = allocated_budget
        elif type_ == "پس‌انداز":
            savings += amount

# بررسی بودجه و گزارش وضعیت مالی
print("📊 گزارش مالی شخصی")
print("-" * 50)
print(f"💰 مجموع درآمد: {income:.2f}")
print(f"💸 مجموع هزینه‌ها: {sum(expenses.values()):.2f}")
print(f"🏦 مجموع پس‌انداز: {savings:.2f}")

# بررسی میزان انحراف از بودجه
print("\n📉 بررسی بودجه هزینه‌ها")
print("-" * 50)
for category, expense in expenses.items():
    allocated = budget.get(category, 0)
    difference = allocated - expense
    status = "✅ در محدوده بودجه" if difference >= 0 else "❌ بیش‌ازحد بودجه"
    print(f"{category}: هزینه {expense:.2f} از بودجه {allocated:.2f} ({status})")
    if difference < 0:
        print(f"  - مقدار اضافی خرج‌شده: {-difference:.2f}")
    else:
        print(f"  - مقدار باقی‌مانده از بودجه: {difference:.2f}")

# بررسی امکان افزایش پس‌انداز
remaining_income = income - sum(expenses.values())
can_save_more = remaining_income > 0
print("\n🏦 بررسی امکان افزایش پس‌انداز")
print("-" * 50)
if can_save_more:
    print(f"✅ امکان افزایش پس‌انداز وجود دارد! مقدار قابل پس‌انداز: {remaining_income:.2f}")
else:
    print("⚠️ امکان افزایش پس‌انداز وجود ندارد، هزینه‌ها با درآمد برابر یا بیشتر است.")

# نمونه خروجی:
# 📊 گزارش مالی شخصی
# --------------------------------------------------
# 💰 مجموع درآمد: 5000000.00
# 💸 مجموع هزینه‌ها: 3200000.00
# 🏦 مجموع پس‌انداز: 1000000.00
#
# 📉 بررسی بودجه هزینه‌ها
# --------------------------------------------------
# خوراک: هزینه 800000.00 از بودجه 1000000.00 (✅ در محدوده بودجه)
#   - مقدار باقی‌مانده از بودجه: 200000.00
# اجاره: هزینه 1500000.00 از بودجه 1500000.00 (✅ در محدوده بودجه)
#   - مقدار باقی‌مانده از بودجه: 0.00
# تفریح: هزینه 900000.00 از بودجه 700000.00 (❌ بیش‌ازحد بودجه)
#   - مقدار اضافی خرج‌شده: 200000.00
#
# 🏦 بررسی امکان افزایش پس‌انداز
# --------------------------------------------------
# ✅ امکان افزایش پس‌انداز وجود دارد! مقدار قابل پس‌انداز: 800000.00
