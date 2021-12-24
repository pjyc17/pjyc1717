import sys; sys.stdin = open('BOJ_7562_나이트의 이동.txt', 'r')

dx = [2,2,1,-1,-2,-2,-1,1]
dy = [1,-1,-2,-2,-1,1,2,2]

for tc in range(1, int(input())+1):
    N = int(input())
    sx, sy = map(int,input().split())
    ex, ey = map(int,input().split())
    # visited = [[0] * N for _ in range(N)]
    x = abs(sx - ex)
    y = abs(sy - ey)
    # if x > y:
    #     key = x
    #     print(key)
    print(y)







24 48
26 49
28 50
29 52
30 50



    25 50
    27 49
    29 50

