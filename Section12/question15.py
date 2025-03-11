import csv
import requests
from io import StringIO

# URL فایل CSV میزبانی شده در اینترنت
csv_url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"

# دریافت داده‌های CSV از اینترنت
response = requests.get(csv_url)
if response.status_code == 200:
    data = response.text  # خواندن محتوای فایل
    csv_file = StringIO(data)  # تبدیل داده‌ها به فایل متنی برای پردازش
    reader = csv.reader(csv_file)

    # پردازش داده‌ها (چاپ هر ردیف در اینجا)
    for row in reader:
        print(row)
else:
    print("خطا در دریافت فایل CSV!")


# داده‌های CSV از اینترنت دریافت شده و هر سطر چاپ شده است.
# نمونه خروجی:
# ['Height(Inches)', 'Weight(Pounds)']
# ['65.78331', '112.9925']
# ['71.51521', '136.4873']
# ['69.39874', '153.0269']
# ...
