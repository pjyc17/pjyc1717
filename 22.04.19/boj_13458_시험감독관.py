import math

N = int(input())
arr = list(map(int, input().split()))
B, C = map(int, input().split())
cnt = 0
for i in range(N):
    cnt += 1
    if arr[i] - B >= 1:
        cnt += math.ceil((arr[i] - B)/C)
print(cnt)