cnt_0 = cnt_1 = 0
for tc in range(1, int(input())+1):
    N = int(input())
    if N == 0:
        cnt_0 += 1
    elif N == 1:
        cnt_1 += 1
if cnt_1 > cnt_0:
    chr = 'cute'
else:
    chr = 'not cute'
print(f'Junhee is {chr}!')