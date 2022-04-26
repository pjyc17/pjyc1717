import sys
input = sys.stdin.readline

def move(direction):
    if direction == 1:
        dir[1], dir[3], dir[6], dir[4] = dir[4], dir[1], dir[3], dir[6]
    elif direction == 2:
        dir[1], dir[3], dir[6], dir[4] = dir[3], dir[6], dir[4], dir[1]
    elif direction == 3:
        dir[1], dir[2], dir[6], dir[5] = dir[5], dir[1], dir[2], dir[6]
    elif direction == 4:
        dir[1], dir[2], dir[6], dir[5] = dir[2], dir[6], dir[5], dir[1]
def axis(direction):
    if direction == 1: return 0, 1
    elif direction == 2: return 0, -1
    elif direction == 3: return -1, 0
    elif direction == 4: return 1, 0

N, M, x, y, k = map(int, input().split())

s = [list(map(int, input().split())) for _ in range(N)]
lst = list(map(int, input().split()))
dir = [0]*7
dir[6] = s[x][y]
for i in range(k):
    r,c = axis(lst[i])
    x = x + r
    y = y + c
    if 0 <= x < N and 0 <= y < M:
        move(lst[i])
        if s[x][y] != 0:
            dir[6] = s[x][y]
            s[x][y] = 0
        else:
            s[x][y] = dir[6]
        print(dir[1])
    else:
        x -= r
        y -= c