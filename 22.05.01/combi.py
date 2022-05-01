lst = ['0', '1', '2', '3']
visited = [0] * len(lst)
ans = []
list = []
def dfs(cnt, list):
    if cnt == len(lst):
        print(''.join(list[:]))
        # ans.append(list[:])
        return
    for i in range(len(lst)):
        if not visited[i]:
            list.append(lst[i])
            visited[i] = 1
            dfs(cnt + 1, list)
            visited[i] = 0
            list.pop()
dfs(0, [])
print(ans)