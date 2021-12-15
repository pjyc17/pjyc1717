for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

def line(r, c, sel_lst):
    if sel_lst[r][c] == 1:
        for d in range(4):
            nr = r+dr[d]
            nc = c+dc[d]
            if N > nr >= 0 and N > nc >= 0:
                if sel_lst[nr][nc] == 0:
                    sel_lst[nr][nc] == 2