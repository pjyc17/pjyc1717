m, n = map(int, input().split())
li = [1]*n
for i in range(2,n):
    if m % i == 0:
        a = i
        b = m // i
        break

if a >= n:
    print('GOOD')
else:
    print('BAD', a)