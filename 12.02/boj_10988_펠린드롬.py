sent = list(map(str, input()))
ans = 1
for i in range(len(sent)//2):
    if sent[i] == sent[len(sent) - 1 - i]:
        ans *= 1
    else:
        ans *= 0
print(ans)