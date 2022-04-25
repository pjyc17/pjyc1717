N = int(input())
lst = [[] * N]
for _ in range(N):
    lst[_+1].append(str(input()))

set(lst)
print(lst)