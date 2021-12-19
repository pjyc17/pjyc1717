import sys
input = sys.stdin.readline
arr = list(input())

n = int(input())
cursor = len(arr)
for _ in range(n):
    arr2 = list(input().split())
    if arr2[0] == 'L':
        if cursor == 0:
            pass
        else:
            cursor -= 1
    elif arr2[0] == 'D':
        if cursor < len(arr):
            cursor += 1
        else:
            pass
    elif arr2[0] == 'B':
        if cursor == 0:
            pass
        else:
            cursor -= 1
            arr.pop(cursor)
    elif arr2[0] == 'P':
        arr.insert(cursor, arr2[1])
        cursor += 1
print(''.join(arr))
