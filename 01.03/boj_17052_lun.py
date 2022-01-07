n = int(input())
arr = input()
ans = 0
if n % 2:
    for i in range(1, n, 2):
        ans += int(arr[i]) * 2 // 10 + int(arr[i]) * 2 % 10
    for i in range(0, n, 2):
        if arr[i] != 'x':
            ans += int(arr[i])
else:
    for i in range(1, n, 2):
        if arr[i] != 'x':
            ans += int(arr[i])
    for i in range(0, n, 2):
        ans += int(arr[i]) * 2 // 10 + int(arr[i]) * 2 % 10
print(ans*9%10)