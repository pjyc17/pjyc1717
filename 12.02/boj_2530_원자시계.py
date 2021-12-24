m, n, l = map(int, input().split())
t = int(input())
print((m+(n+(l+t)//60)//60)%24, (n+(l+t)//60)%60,(t+l)%60)
