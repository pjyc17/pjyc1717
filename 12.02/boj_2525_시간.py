m,n = map(int, input().split())
l = int(input())
print((m+((n+l)//60))%24, (n+l)%60)
