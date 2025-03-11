# 6. یک کاربر خاص براساس شناسه id حذف کنید.
import sqlite3

import sqlite3

# اتصال به پایگاه داده
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# شناسه کاربری که می‌خواهید حذف کنید
user_id = 1

# حذف کاربر بر اساس شناسه (id)
cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
conn.commit()

print(f"User with id {user_id} deleted successfully!")

# بستن اتصال
conn.close()

