# 7. یک تاپل شامل مختصات چند نقطه در فضا بسازید و فاصله میانگین نقاط را از مبدا پیدا کنید

import math

points = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

def euclidean_distance(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

# نمونه استفاده :
distances = tuple(euclidean_distance(points[i], points[i + 1]) for i in range(len(points) - 1))
print(distances)

# Output > (5.196152422706632, 5.196152422706632)