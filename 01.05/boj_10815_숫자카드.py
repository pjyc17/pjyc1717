import sys
input = sys.stdin.readline

N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))
for i in arr2:
    if i in arr1:
        print(1, end=' ')
    else:
        print(0, end=' ')

### 시간초과