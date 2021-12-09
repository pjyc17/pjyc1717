for tc in range(1, int(input())+1):
    m, n = map(int, input().split())
    mul = 1
    for i in range(min(m,n), 0, -1):
        if m % i == 0 and n % i == 0 and mul <= min(m,n):
            mul *= i
            m //= i
            n //= i
        
    print(mul*m*n)

a = int(input())
L = []
for x in range(0, a):
    L.append(list(map(int,input().split(' '))))
for n in range(0, a):
    n1 = L[n][0]
    n2 = L[n][1]
    res = n1 * n2
    while(n2!=0):
        r = n1%n2
        n1= n2
        n2= r
    print(res // n1)
n = int(input())

def gcd(x,y):
    mod = x%y
    while mod>0:
        x=y
        y=mod
        mod = x%y
    return y

def lcm(x,y):
    return x * y // gcd(x,y)

a= []
for _ in range(n):
    n1, n2 = map(int, input().split())
    a.append(lcm(n1,n2))

for i in a:
    print(i)

def Euclid(a, b):
    big, small = max(a, b), min(a, b)
    if big % small == 0:
        return small
    return Euclid(small, big%small)

N = int(input())
ans = []
for _ in range(N):
    a, b = map(int, input().split())
    GCF = Euclid(a, b)
    ans.append(GCF * a//GCF * b//GCF)

print(*ans, sep="\n")