# 4. بازیابی و چاپ تمام رکوردها از کاربران

import sqlite3

# اتصال به پایگاه داده
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# نمایش دیتای جدول
for row in rows:
    print(row)

# بستن اتصال
conn.close()
