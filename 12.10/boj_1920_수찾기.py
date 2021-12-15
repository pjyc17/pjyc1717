N = int(input())
A = set(input().split())
M = int(input())
X = input().split()
print(A)
print(X)
for i in X:
    if i in A:
        print(1)
    else:
        print(0)
# input();a=set(input().split())
# input();m=input().split()
# for i in m: print("1" if i in a else "0")