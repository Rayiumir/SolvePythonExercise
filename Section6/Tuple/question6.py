import math

# تعریف یک tuple دو بعدی شامل مختصات
points = ((2, 3), (7, 1))

# استخراج مختصات دو نقطه
(x1, y1), (x2, y2) = points

# محاسبه فاصله بین دو نقطه با فرمول فاصله اقلیدسی
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# نمایش فاصله
print("فاصله بین دو نقطه:", distance)

# --------------------------
# خروجی:
# فاصله بین دو نقطه: 5.385164807134504
# --------------------------
