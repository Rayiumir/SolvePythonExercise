# 4. یک دیکشنری از نام ها و شماره تلفن ایجاد کنید، سپس آنها را به ترتیب حروف الفبا چاپ کنید

contacts = {
    "Reza": "09123456789",
    "Ali": "09211234567",
    "Mina": "09334567890"
}

sorted_contacts = dict(sorted(contacts.items()))
for name, phone in sorted_contacts.items():
    print(f"{name}: {phone}")

# Output
# Ali: 09211234567
# Mina: 09334567890
# Reza: 09123456789