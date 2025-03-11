import csv

# خواندن اطلاعات مشتریان از فایل customers.csv
customers = {}
with open("customers.csv", mode="r", encoding="utf-8") as cust_file:
    reader = csv.DictReader(cust_file)
    for row in reader:
        # فرض بر این است که ستون مشتریان با نام "CustomerID" ذخیره شده است
        customers[row["CustomerID"]] = row

# خواندن اطلاعات سفارشات از فایل orders.csv و ترکیب آن با اطلاعات مشتریان
combined_data = []
with open("orders.csv", mode="r", encoding="utf-8") as orders_file:
    reader = csv.DictReader(orders_file)
    for order in reader:
        cust_id = order["CustomerID"]
        if cust_id in customers:
            # ترکیب اطلاعات سفارش (order) و مشتری (customer)
            # در اینجا اگر کلیدهای مشابه وجود داشته باشند، اطلاعات مشتری بر اطلاعات سفارش ترجیح داده می‌شود.
            combined_row = {**order, **customers[cust_id]}
            combined_data.append(combined_row)

# تعیین سرستون‌های فایل ترکیبی (ترکیبی از کلیدهای موجود در اولین ردیف)
if combined_data:
    headers = list(combined_data[0].keys())
else:
    headers = []

# ذخیره داده‌های ترکیبی در فایل combined.csv
with open("combined.csv", mode="w", encoding="utf-8", newline="") as combined_file:
    writer = csv.DictWriter(combined_file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(combined_data)

print("فایل 'combined.csv' با موفقیت ایجاد شد.")

# نمونه ورودی:
# فایل customers.csv:
# CustomerID,Name,Email
# 1,Ali,ali@example.com
# 2,Sara,sara@example.com
# 3,Reza,reza@example.com
#
# فایل orders.csv:
# OrderID,CustomerID,OrderDate,Total
# 1001,1,2025-01-01,150.00
# 1002,2,2025-01-02,200.00
# 1003,1,2025-01-03,50.00
#
# نمونه خروجی (محتوای فایل combined.csv):
# OrderID,CustomerID,OrderDate,Total,Name,Email
# 1001,1,2025-01-01,150.00,Ali,ali@example.com
# 1002,2,2025-01-02,200.00,Sara,sara@example.com
# 1003,1,2025-01-03,50.00,Ali,ali@example.com
