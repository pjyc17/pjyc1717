import sys
input = sys.stdin.readline
n = int(input())
lst = []
for i in range(n):
    arr = list(input().split())
    if arr[0] == 'push':
        lst.append(int(arr[1]))
    elif arr[0] == 'pop':
        if lst:
            m = lst.pop(0)
            print(m)
        else:
            print(-1)
    elif arr[0] == 'size':
        print(len(lst))
    elif arr[0] == 'empty':
        if lst:
            print(0)
        else:
            print(1)
    elif arr[0] == 'front':
        if lst:
            print(lst[0])
        else:
            print(-1)
    elif arr[0] == 'back':
        if lst:
            print(lst[-1])
        else:
            print(-1)