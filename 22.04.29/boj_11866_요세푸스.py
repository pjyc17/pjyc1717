import sys
input = sys.stdin.readline
n, m = map(int,input().split())
lst = [i for i in range(1, n+1)]
for i in lst:
    q = lst.pop()