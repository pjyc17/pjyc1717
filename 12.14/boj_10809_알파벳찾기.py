sentence = input()
cnt = 1
arr = [-1 for _ in range(26)]

for i in range(len(sentence)):
    if arr[ord(sentence[i]) -97] == -1:
        arr[ord(sentence[i]) -97] += cnt
    cnt += 1
for i in range(26):
    print(arr[i], end=' ')