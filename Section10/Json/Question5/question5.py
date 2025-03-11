import json
from datetime import datetime

# آدرس فایل JSON که شامل تاریخ تولد افراد است
file_path = "birthdays.json"

# خواندن داده‌ها از فایل JSON
with open(file_path, "r", encoding="utf-8") as file:
    people = json.load(file)

# استخراج افرادی که تاریخ تولدشان در ماه تیر (ماه 7 میلادی) است

tir_birthdays = [
    person for person in people
    if datetime.strptime(person["تاریخ_تولد"], "%Y-%m-%d").month == 7
]

# نمایش اطلاعات افرادی که تاریخ تولدشان در ماه تیر است
print("افرادی که تاریخ تولدشان در ماه تیر است:")
for person in tir_birthdays:
    print(f"نام: {person['نام']}, تاریخ تولد: {person['تاریخ_تولد']}")

# خروجی :
# افراد که تاریخ تولدشان در ماه تیر است:
# نام: علی, تاریخ تولد: 2004-07-10
# نام: سارا, تاریخ تولد: 2003-07-20
# نام: نرگس, تاریخ تولد: 2006-07-05
