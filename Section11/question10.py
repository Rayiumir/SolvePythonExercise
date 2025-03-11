# 10. حذف جدول کاربران

import sqlite3

# اتصال به پایگاه داده
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# به جدول درخواست می فرسته که جدول users را حذف کند.
cursor.execute("DROP TABLE IF EXISTS users")

# ثبت و بستن اتصال
conn.commit()
conn.close()
