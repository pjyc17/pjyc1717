import sys
input = sys.stdin.readline
lst = []
for i in range(int(input())):
    n, m = map(str,input().split())
    n = int(n)
    lst.append((n, i, m))
ans = sorted(lst)
for i, j, k in ans:
    print(i, k)