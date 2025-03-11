import csv

# نام فایل CSV که شامل اطلاعات تراکنش‌ها است
csv_filename = "transactions.csv"

# متغیرها برای ذخیره مجموع درآمدها و هزینه‌ها
total_income = 0
total_expense = 0

# خواندن فایل CSV
with open(csv_filename, newline='', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # خواندن هدر (نام ستون‌ها)

    for row in reader:
        date_str, transaction_type, amount, description = row
        amount = float(amount)  # تبدیل مقدار به عدد

        if transaction_type.lower() == "income":  # بررسی نوع تراکنش
            total_income += amount
        elif transaction_type.lower() == "expense":
            total_expense += amount

# محاسبه سود یا زیان
net_profit = total_income - total_expense

# نمایش گزارش مالی
print("گزارش مالی تراکنش‌ها")
print("-" * 30)
print(f"مجموع درآمدها  : {total_income:.2f}")
print(f"مجموع هزینه‌ها  : {total_expense:.2f}")
print(f"سود / زیان      : {net_profit:.2f}")

# نمونه خروجی:
# گزارش مالی تراکنش‌ها
# ------------------------------
# مجموع درآمدها  : 50000.00
# مجموع هزینه‌ها  : 32000.00
# سود / زیان      : 18000.00
