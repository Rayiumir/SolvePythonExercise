import csv


# تعریف تابع برای پردازش هر خط (مثلاً محاسبه مجموع یک ستون عددی)
def process_row(row):
    try:
        value = float(row["Amount"])  # فرض: مقدار عددی در ستون 'Amount' قرار دارد
        return value * 1.1  # مثلا افزایش 10 درصدی مقدار
    except ValueError:
        return None  # در صورت وجود مقدار نامعتبر


# خواندن و پردازش فایل CSV به‌صورت خط‌به‌خط
file_path = "large_file.csv"
with open(file_path, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        result = process_row(row)
        if result is not None:
            print(f"Original: {row['Amount']}, Processed: {result:.2f}")
