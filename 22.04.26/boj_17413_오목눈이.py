s = str(input()) + ' '
cnt = 1
lst = []
for i in s:
    if i == ' ':
        print(lst[::-1])
        lst = []
    lst.append(i)