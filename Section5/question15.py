# 15. محاسبه و چاپ حد بالایی عدد اول k-ام

import math

def upper_bound_kth_prime(k): # بالای k-امین عدد اول را تخمین می زند.
    # تقریب اولیه با استفاده از قضیه اعداد اول
    x = k * math.log(k) + k * math.log(math.log(k))
    
    # پالایش (برای دقت بهتر در صورت نیاز تنظیم کنید)
    x *= 1.1  

    return int(x)


# نمونه استفاده
k = 100  # بالایی را برای صدمین عدد اول پیدا کنید
upper_bound = upper_bound_kth_prime(k)
print(f"Estimated upper bound for the {k}th prime number: {upper_bound}")

# Output > Estimated upper bound for the 100th prime number: 674

