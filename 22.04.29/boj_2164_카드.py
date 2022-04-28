from collections import deque

n = int(input())
q = deque([])
for i in range(n):
    q.append(i+1)
while q:
    if len(q) == 1:
        print(q[0])
        break
    q.popleft()
    p = q.popleft()
    q.append(p)