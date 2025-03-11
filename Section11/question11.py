# 11. ذخیره رمزهای عبور ایمن با استفاده از bcrypt

import bcrypt

# ایکد کردن عبارت پسورد
password = "mypassword".encode("utf-8")

# هش کردن پسورد
hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

# نمایش پسورد هش شده
print("Hashed Password:", hashed_password.decode())


