chr = str(input())
ans = 10
for i in range(1, len(chr)):
    if chr[i] == chr[i-1]:
        ans += 5
    elif chr[i] != chr[i-1]:
        ans += 10
print(ans)