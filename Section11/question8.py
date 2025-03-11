# 8. بررسی اینکه آیا کاربر خاص در جدول وجود دارد یا خیر

import sqlite3

# اتصال به پایگاه داده
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# بررسی وجود کاربر خاص 
cursor.execute("SELECT EXISTS(SELECT 1 FROM users WHERE name = ?)", ("Ali",))
exists = cursor.fetchone()[0]

# این شرط بررسی می کند که کاربر وجود دارد یا خیر را نمایش دهد.
if exists:
    print("User exists")
else:
    print("User does not exist")

# بستن اتصال
conn.close()
