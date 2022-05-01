from re import I


n, m = map(int,input().split())

def fac(num):
    if num>1:
        return num * fac(num-1)
    else:
        return 1
        

print(int(fac(n)/fac(m)/fac(n-m))%10007)