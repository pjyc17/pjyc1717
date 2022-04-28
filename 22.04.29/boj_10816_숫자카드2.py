import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
m = int(input())
chk = list(map(int, input().split()))

for i in range(len(chk)):
    print(lst.count(chk[i]), end=' ')

# from collections import Counter
# from sys import stdin

# n = stdin.readline().rstrip()
# card = list(map(int,stdin.readline().split()))
# m = stdin.readline().rstrip()
# test = list(map(int,stdin.readline().split()))

# count = Counter(card)

# for i in range(len(test)):
#     if test[i] in count:
#         print(count[test[i]], end=' ')
#     else:
#         print(0, end=' ')