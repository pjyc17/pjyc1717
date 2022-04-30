# n = int(input())
# cnt = 0
# min_ = 1e9
# def cho(cnt, n, div3, div2, min1):
#     global min_
#     while True:
#         if n == 1:
#             min_ = min(min_, cnt)
#             return

#         if div3 >= 0 and n % 3 == 0:
#             cho(cnt + 1, int(n/3), div3 + 1, div2, min1)
#         if div2 >= 0 and n % 2 == 0:
#             cho(cnt + 1, int(n/2), div3, div2 + 1, min1)
#         if min1 >= 0:
#             cho(cnt + 1, n - 1, div3 + 1, div2, min1 + 1)
# cho(0, n, 0, 0, 0)
# print(cnt)
import sys
input = sys.stdin.readline
n = int(input())
dp = [0] * 1000001
for i in range(2, n+1):
    dp[i] = dp[i-1]+1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[n])
