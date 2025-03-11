import math

# ایجاد tuple از مختصات نقاط
points = ((1, 2), (4, 6), (7, 8))

# استخراج مختصات اولین و آخرین نقطه
first_point = points[0]
last_point = points[-1]

# محاسبه فاصله بین اولین و آخرین نقطه
distance = math.sqrt((last_point[0] - first_point[0])**2 + (last_point[1] - first_point[1])**2)

# نمایش نتیجه
print("فاصله بین اولین و آخرین نقطه:", distance)

# نمونه خروجی:
# فاصله بین اولین و آخرین نقطه: 7.810249675906654
