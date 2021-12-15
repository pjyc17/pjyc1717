sen = list(input())

lst = []
ans = []
for i in range(1, len(sen)-1):
    for j in range(1+i, len(sen)):
        a = sen[:i]
        b = sen[i:j]
        c = sen[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        lst.append(a+b+c)
for i in lst:
    ans.append(''.join(i))
print(sorted(ans)[0])


