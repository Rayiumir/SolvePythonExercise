# 3. درج یک رکورد جدید در جدول کاربران

import sqlite3

# اتصال به پایگاه داده
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# افزودن دیتا به users
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Ali", 25))

# ثبت و بستن اتصال
conn.commit()
conn.close()
