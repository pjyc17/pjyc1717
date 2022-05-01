n, m = map(int, input().split())
lst = input().split()
lst.sort()
arr = []
visited = [0] * m
def sol(x, idx):
    if x == n:
        vo = 0
        co = 0
        for i in range(n):
            if arr[i] in 'aeiou': vo += 1
            else: co += 1
        if vo > 0 and co > 1:
            print(''.join(arr))
    for i in range(idx, m):
        if not visited[i]:
            arr.append(lst[i])
            visited[i] = 1
            sol(x + 1, )