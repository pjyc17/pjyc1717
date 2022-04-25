import sys
input = sys.stdin.readline
N, M = map(int, input().split())

lst = [list(map(str, input().strip())) for _ in range(N)]
ans_list = []
def find(x, y):
    cnt1 = 0
    for i in range(x,x+8):
        for j in range(y,y+8):
            if (i+j) % 2 == 0 and lst[i][j] != 'B':
                cnt1 += 1
            if (i+j) % 2 == 1 and lst[i][j] != 'W':
                cnt1 += 1
    ans_list.append(cnt1)
    ans_list.append(64 - cnt1)
for i in range(0, N - 7):
    for j in range(0, M - 7):
        find(i, j)            
# cnt2 = 0
# for i in range(0,N):
#     for j in range(0,M):
#         if (i+j) % 2 == 0 and lst[i][j] != 'W':
#             cnt2 += 1
#         if (i+j) % 2 == 1 and lst[i][j] != 'B':
#             cnt2 += 1
            

print(min(ans_list))