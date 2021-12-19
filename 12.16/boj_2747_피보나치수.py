n = int(input())
lst = []
for i in range(n):
    if i == 0:
        lst.append(0)
    elif i == 1:
        lst.append(1)
    else:
        lst.append()

n = int(input())
a, b = 0, 1
for i in range(n):
    a, b = b, a+b
print(a)