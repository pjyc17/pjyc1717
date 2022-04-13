k, n = map(int, input().split())
tot = 0
lst = []

for i in range(k):
    a = int(input())
    tot += a
    lst.append(a)
mok = n // tot
mok1 = mok
ans = 0
while True:
    if ans == n:
        print(mok1)
        break
    ans = 0
    mok1 -= 1
    for i in range(k):
        ans += lst[i] // mok1
