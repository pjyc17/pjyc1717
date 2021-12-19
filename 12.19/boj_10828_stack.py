import sys
input = sys.stdin.readline
n = int(input())
lst = []
for _ in range(n):
    arr = list(input().split())
    if arr[0] == 'push':
        lst.append(arr[1])

    elif arr[0] == 'pop':
        if lst:
            m = lst.pop()
            print(m)
        else:
            print(-1)
    elif arr[0] == 'top':
        if lst:
            print(lst[-1])
        else:
            print(-1)
    elif arr[0] == 'size':
        print(len(lst))
    else:
        if lst:
            print(0)
        else:
            print(1)