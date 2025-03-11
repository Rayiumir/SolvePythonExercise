# 3. یک تاپل با چند تاپل ایجاد کنید و مجموع هر تاپل داخلی را محاسبه کنید

tuples = ((1, 2, 3), (4, 5), (6,))
sums = tuple(sum(t) for t in tuples)
print(sums)  

# Output: (6, 9, 6)
