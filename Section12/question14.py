import csv
import sqlite3

# ایجاد اتصال به دیتابیس SQLite (در صورت عدم وجود، فایل دیتابیس ایجاد می‌شود)
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# ایجاد جدول (در صورت عدم وجود)
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT,
    price INTEGER
)
""")

# خواندن داده‌ها از فایل CSV و وارد کردن به دیتابیس
csv_file = "products.csv"

with open(csv_file, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("INSERT INTO products (name, category, price) VALUES (?, ?, ?)",
                       (row["نام"], row["دسته‌بندی"], int(row["قیمت"])))

# ذخیره تغییرات و بستن اتصال
conn.commit()
conn.close()


 # داده‌ها از فایل products.csv خوانده شده و به دیتابیس SQLite منتقل شدند.

