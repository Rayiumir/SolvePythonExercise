# 5. بازیابی یک کاربر خاص با سن

import sqlite3

import sqlite3

# اتصال به پایگاه داده
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# جستجوی کاربر با نام "Ali"
cursor.execute("SELECT * FROM users WHERE name = ?", ("Ali",))
user = cursor.fetchone()

if user:
    # تغییر سن کاربر "Ali" (مثال: 30)
    cursor.execute("UPDATE users SET age = ? WHERE name = ?", (30, "Ali"))
    conn.commit()
    print("Age updated successfully!")
else:
    print("User not found.")

# بستن اتصال
conn.close()

