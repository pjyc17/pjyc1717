n = int(input())
arr = list(map(int, input().split()))

max_ = -1000000
min_ = 1000000
for i in range(n):
    if max_ <= arr[i]:
        max_ = arr[i]
    if min_ >= arr[i]:
        min_ = arr[i]
print(min_, max_)