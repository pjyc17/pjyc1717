import sys
input = sys.stdin.readline
m,n = map(int, input().split())
lst = list(map(int, input().split()))

def plus(a,b):
    sum = 0
    for i in range(a-1, b):
        sum += lst[i]
    return sum
sum_a = sum_b = 0
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(0, a-1):
        sum_a += lst[i]
    