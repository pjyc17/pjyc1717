dir = {0 : (1,0), 1 : (0,-1), 2 : (-1,0), 3 : (0,1)}

N = int(input())
applePoint = int(input())
graph = [list(map(int, input().split()))]
for i in range(applePoint):
    x, y = map(int, input().split())
