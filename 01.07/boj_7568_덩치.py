n = int(input())
arr = []
ans = [1] * n
for _ in range(n):
    m,k = map(int, input().split())
    arr.append((m,k))

for i in range(n):
    for j in range(i+1, n):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            ans[i] += 1
        elif arr[i][0] > arr[j][0] and arr[i][1] > arr[j][1]:
            ans[j] += 1
for i in ans:
    print(i, end=" ")