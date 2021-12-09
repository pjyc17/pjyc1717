lst = []
for tc in range(1, int(input())+1):
    m, n ,l = map(int, input().split())
    if m == n == l:
        lst.append(10000+ 1000*m)
    elif m == n != l:
        lst.append(1000+100*m)
    elif m == l != n:
        lst.append(1000+100*m)
    elif l == n != m:
        lst.append(1000+100*n)
    else:
        lst.append(100*max(m,n,l))
print(max(lst))
# short code 
# l=sorted(list(map(int,input().split())))
# s=len(set(l))
# print(l[s-1]*[100,1000][s==1]+[10000,1000,0][s-1]) 
