# تعریف دی‌کشنری با نام افراد و شماره‌های تماس آنها
contacts = {
    "Ali": "09121234567",
    "Sara": "09129876543",
    "Reza": "09137654321",
    "Niloofar": "09134876543"
}

# جستجوی شماره تماس فرد با نام خاص
name_to_search = "Sara"
phone_number = contacts.get(name_to_search, "شماره تماس یافت نشد")

# نمایش شماره تماس
print(f"شماره تماس {name_to_search}: {phone_number}")

# نمونه خروجی:
# شماره تماس Sara: 09129876543
