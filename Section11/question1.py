# 1. ایجاد یک پایگاه داده SQLite جدید (example.db)

import sqlite3

# ایجاد و اتصال به پایگاه داده 
conn = sqlite3.connect("example.db")

# بستن اتصال
conn.close()
