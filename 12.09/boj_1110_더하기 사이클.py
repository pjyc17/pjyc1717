N = int(input())
nex = N
cnt = 0
while 1:
    a = nex // 10
    b = nex % 10
    c = (a + b) % 10
    nex = (b*10) + c

    cnt += 1
    if N == nex:
        break
print(cnt)
