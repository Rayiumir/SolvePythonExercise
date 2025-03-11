import math

# 14. تبدیل سال به ماه, روز و ساعت

years = 1  # تبدیل ۱ سال
days_in_year = 365  # ۱ سال برابر با ۳۶۵ روز
months_in_year = 12  # ۱ سال برابر ۱۲ ماه
hours_in_day = 24  # ۱ روز برابر با ۲۴ ساعت

months = years * months_in_year
days = years * days_in_year
hours = days * hours_in_day

print("Months:", months)
print("Days:", days)
print("Hours:", hours)

# Output > Months: 12 - Days: 365 - Hours: 8760