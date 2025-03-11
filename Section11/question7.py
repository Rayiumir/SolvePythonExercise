# 7. جستجو کاربران بالای 18 سال

import sqlite3

# اتصال به پایگاه داده
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# جستجو کاربر با سن بالای ۱۸ سال
cursor.execute("SELECT * FROM users WHERE age > 18")
rows = cursor.fetchall()

# نمایش دیتا
for row in rows:
    print(row)

# بستن اتصال
conn.close()
