n, m = map(int, input().split())
lst = list(map(str, input().split()))
lst.sort()
visited = [0] * m
# from collections import deque

# q = deque()
# for i in range(m):
#     if len(q) == 4:
#         for i in q:
#             print(i, end='')
#         print()
#     if visited[i] == 0:
#         q.append(lst[i])
#         visited[i] = 1
def dfs(x, cnt):
    ans_list = []
    if cnt == 4:
        for i in range(4):
            print(ans_list[i], end='')
        print()
        return
    for i in 