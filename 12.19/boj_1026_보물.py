n = int(input())
arr = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

arr.sort()
arr2.sort()
ans = 0
for i in range(n):
    ans += arr[i]*arr2[n-1-i]
print(ans)