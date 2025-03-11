import math

# 18: محاسبه تعداد موکول ها در جرم مشخصی از ماده
mass = 18  # جرم نمونه بر حسب گرم
molar_mass = 18  # جرم مولی نمونه بر حسب گرم بر مول g/mol
avogadro_number = 6.022e23  # ثابت آووگادرو (مولکول در هر مول)

# فرمول تعداد مول: مول = جرم / جرم_مولری
moles = mass / molar_mass

# فرمول تعداد مولکول: مولکول = مول * عدد آووگادرو
molecules = moles * avogadro_number
print("Number of Molecules:", molecules)

# Output > Number of Molecules: 6.022e+23