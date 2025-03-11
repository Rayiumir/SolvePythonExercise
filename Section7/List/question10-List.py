# 10. اعداد تصادفی به ترتیب صعودی، نزولی و تصادفی مرتب شده اند

import random

def random_list(n):
  random_numbers = [random.randint(1,100) for i in range(n)]
  random_numbers.sort()
  random_numbers_desc = sorted(random_numbers, reverse=True)
  random.shuffle(random_numbers_desc)
  return random_numbers, random_numbers_desc, random_numbers_desc

# نمونه استفاده:

n = 5
asc, desc, shuffled = random_list(n)
print("Random list (n=5):")
print("Ascending:", asc)
print("Descending:", desc)
print("Shuffled:", shuffled)

# Output
# Random list (n=5):
# Ascending: [19, 19, 23, 28, 79]
# Descending: [28, 23, 79, 19, 19]
# Shuffled: [28, 23, 79, 19, 19]