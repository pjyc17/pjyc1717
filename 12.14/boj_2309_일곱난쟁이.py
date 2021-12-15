arr = [int(input()) for _ in range(9)]

for i in range(0, 8):
    for j in range(i+1, 9):
        ans = sum(arr) - arr[i] - arr[j]
        if ans == 100:
            idx_1 = i
            idx_2 = j
arr.remove(arr[idx_1])
arr.remove(arr[idx_2-1])
for i in range(7):
    print(sorted(arr)[i])