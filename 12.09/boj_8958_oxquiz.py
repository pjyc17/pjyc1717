for tc in range(1, int(input())+1):
    chr = str(input())
    cnt = 0
    ans = 0
    for i in range(len(chr)):
        if chr[i] == 'O':
            cnt += 1
            ans += cnt
        else:
            cnt = 0
    print(ans)