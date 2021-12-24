m = int(input())
n = 1
while True:
    if 2*m >= n*(n+1):
        n += 1
        pass
    elif 2*m <= n*(n+1):
        print(n-1)
        break