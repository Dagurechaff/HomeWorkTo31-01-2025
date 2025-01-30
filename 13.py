import itertools 
count = 0
s = itertools.product([0,1],repeat = 11)
for i in s:
    if (8 + sum(i))%5 !=0:
        count += 1
print(count)