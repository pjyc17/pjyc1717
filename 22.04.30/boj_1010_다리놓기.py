for tc in range(int(input())):
    N, M = map(int, input().split())
    ans = 1
    per = 1
    for i in range(N):
        ans *= (M-i)
        per *= (i+1)
    print(ans//per)