# cnt = 0
# n = int(input())
# for _ in range(8):
#     a = int(input())
#     if n <= a:
#         n = a
# print(n)

arr = [int(input()) for _ in range(9)]
max_ = arr[0]
for i in range(9):
    if arr[i] >= max_:
        max_ = arr[i]
        idx = i
print(max_)
print(idx+1)