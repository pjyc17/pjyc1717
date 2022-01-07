import sys
input = sys.stdin.readline
arr = [0] * 10001

for t in range(int(input())):
    arr[int(input())] += 1
for i in range(1, 10001):
    for j in range(arr[i]):
        print(i)
