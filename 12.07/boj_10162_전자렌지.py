N = int(input())
if N % 10:
    print(-1)
else:
    min_5 = N // 300
    min_1 = (N % 300) // 60
    sec_10 = (N % 60) // 10
    print(min_5, min_1, sec_10)