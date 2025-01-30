for i in range(101000000, 102000000 + 1):
    if i % 2 == 0:
        c = 1
        s = round(i ** 0.5)
        for j in range(2, s + 1):
            if i % j == 0:
                if j % 2 == 0:
                    c += 1
                k = i // j
                if k % 2 == 0:
                    c += 1
                    if j == k:
                        c -= 1
                if c > 3:
                    break
        if c == 3:
            print(i)
