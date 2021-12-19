arr = list(map(str, input()))
lst = [0] * 26

for i in arr:
    if 122 >= int(ord(i)) >= 97:
        lst[int(ord(i))-97] += 1
    elif 65 <= int(ord(i)) <= 90:
        lst[int(ord(i))-65] += 1
cnt = 0
for i in range(26):
    if max(lst) == lst[i]:
        cnt += 1
        idx = i
if cnt == 1:
    print(chr(int(idx+65)))
else: print('?')