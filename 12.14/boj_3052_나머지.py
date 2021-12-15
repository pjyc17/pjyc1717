arr = [int(input()) for _ in range(10)]

lst = []
for i in range(10):
    if arr[i] % 42 not in lst:
        lst.append(arr[i] % 42)
print(len(lst))