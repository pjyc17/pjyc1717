tc = int(input())
chr = str(input())
cta = ctb = 0
for i in range(len(chr)):
    if chr[i] == 'A':
        cta += 1
    else:
        ctb += 1
if cta > ctb:
    print('A')
elif ctb > cta:
    print('B')
else:
    print('Tie')