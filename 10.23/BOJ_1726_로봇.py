import sys; sys.stdin = open('BOJ_1726_로봇.txt','r')
from collections import deque

r, c = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(r)]
spoint = list(map(int, input().split()))
epoint = list(map(int, input().split()))
# 동 1 서 2 남 3 북 4
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
q = deque
for i in range(3):
    r = spoint[i] - epoint[i]
    print(r)
# 가장 먼저 해야할 일 dfs구현하기

def dfs(r,c,dir):
    arr[r][c] == 1