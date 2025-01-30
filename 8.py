from itertools import product
k = 0
for i in product('белка', repeat = 4):
    if i.count('б') == 1:
        k += 1
print(k)
