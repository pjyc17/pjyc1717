import sys
input = sys.stdin.readline
n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]

ans = sorted(lst)

for i in range(n):
    for j in range(2):
        print(ans[i][j], end=' ')
    print()