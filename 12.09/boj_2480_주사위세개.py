m, n ,l = map(int, input().split())
if m == n == l:
    print(10000+ 1000*m)
elif m == n != l:
    print(1000+100*m)
elif m == l != n:
    print(1000+100*m)
elif l == n != m:
    print(1000+100*n)
else:
    print(100*max(m,n,l))
# short code 
# l=sorted(list(map(int,input().split())))
# s=len(set(l))
# print(l[s-1]*[100,1000][s==1]+[10000,1000,0][s-1]) 
