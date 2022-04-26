from collections import deque
from sys import stdin
input = stdin.readline
N = int(input())
q = deque()
for _ in range(N):
    quest= list(map(str,input().split()))

    if 'push_front' == quest[0]:
        q.insert(0, quest[1])

    elif 'push_back' == quest[0]:
        q.append(quest[1])
    elif 'front' == quest[0]:
        if q:
            print(q[0])
        else:
            print(-1)
    elif 'back' == quest[0]:
        if q:
            print(q[-1])
        else:
            print(-1)
    elif 'size' == quest[0]:
        print(len(q))
    elif 'pop_front' == quest[0]:
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif 'pop_back' == quest[0]:
        if q:
            print(q.pop())
        else:
            print(-1)
    elif 'empty' == quest[0]:
        if len(q) == 0:
            print(1)
        else:
            print(0)