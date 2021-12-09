h, m = map(int,input().split())
if m - 45 < 0:
    h -= 1
    m += 15
    if h - 1 < 0:
        h += 24
        h %= 24
elif m - 45 >= 0:
    m -= 45
print(h, m)