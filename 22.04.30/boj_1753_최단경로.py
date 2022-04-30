import sys
input = sys.stdin.readline
v, e = map(int, input().split())
start = int(input())
lst = [list(map(int, input().split())) for _ in range(e)]
near_lst = [dict() for _ in range(v+1)]

for data in lst:
    s,e,w = data
    if near_lst[s].get(e) == None:
        near_lst[s][e] = w
    else:
        near_lst[s][e] = min(near_lst[s][e], w)

value = [1e9] *(v+1)
value[start] = 0
from collections import deque
q = deque()
q.append(start)
while q:
    p = q.popleft()
    for node in near_lst[p]:
        if value[node] > value[p] + near_lst[p][node]:
            value[node] = value[p] + near_lst[p][node]
            q.append(node)

for i in range(1, len(value)):
    if value[i] >= int(1e9):
        print('INF')
    else:
        print(value[i])