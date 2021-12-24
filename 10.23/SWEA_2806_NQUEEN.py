import sys; sys.stdin = open('SWEA_2806_NQUEEN.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    dr = [0,1,1,1,0,-1,-1,-1]
    dc = [1,1,0,-1,-1,-1,0,1]
    arr = [[0] * N for _ in range(N)]
    
    