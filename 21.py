def f(x, h):
    if (h == 3 or h == 5) and x >= 46:
        return 1
    elif h == 5 and x < 46:
        return 0
    elif x >= 46 and h < 5:
        return 0
    else:
        if h % 2 == 0:
            return f(x + 1, h + 1) or f(x + 2, h + 1) or f(x * 3, h + 1)
        else:
            return f(x + 1, h + 1) and f(x + 2, h + 1) and f(x * 3, h + 1)

def f1(x, h):
    if h == 3 and x >= 46:
        return 1
    elif h == 3 and x < 46:
        return 0
    elif x >= 46 and h < 3:
        return 0
    else:
        if h % 2 == 0:
            return f1(x + 1, h + 1) or f1(x + 2, h + 1) or f1(x * 3, h + 1)
        else:
            return f1(x + 1, h + 1) and f1(x + 2, h + 1) and f1(x * 3, h + 1)

for x in range(1, 46):
    if f(x, 1) == 1:
        print(x)
print('----')
for x in range(1, 46):
    if f1(x, 1) == 1:
        print(x)
