from re import I


n,m = map(int,input().split())
ans = 1
for i in range(n, n-m,-1):
    ans *= i
for i in range(m, 0, -1):
    ans /= i
print(int(ans))
