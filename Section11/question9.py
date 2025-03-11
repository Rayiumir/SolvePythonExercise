# 9. شمارش تعداد کل کاربران

import sqlite3

# اتصال به پایگاه داده
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# بررسی می کند چه تعداد کاربر در جدول وجود دارد
cursor.execute("SELECT COUNT(*) FROM users")
count = cursor.fetchone()[0]

# نمایش دیتا
print("Total users:", count)

# بستن اتصال
conn.close()


