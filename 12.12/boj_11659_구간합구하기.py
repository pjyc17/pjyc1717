import sys
input = sys.stdin.readline
m, n = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(n):
    a, b = map(int,input().split())
    ans = 0
    for i in range(a-1,b):
        ans += arr[i]
    print(ans)