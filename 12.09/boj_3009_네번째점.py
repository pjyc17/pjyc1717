lst_m = []
lst_n = []
for _ in range(3):
    m, n = map(int,input().split())
    lst_m.append(m)
    lst_n.append(n)

lst_m.sort()
lst_n.sort()
for i in range(3):
    if lst_m[i] != lst_m[1]:
        print(lst_m[i], end=' ')
for i in range(3):
    if lst_n[i] != lst_n[1]:
        print(lst_n[i])