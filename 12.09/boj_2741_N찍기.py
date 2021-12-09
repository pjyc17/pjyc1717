# for i in range(int(input())):
#     print(i+1)

# for i in range(int(input()),0,-1):
#     print(i)

# for _ in range(1,int(input())+1):
#     print('*'*_)

N = int(input())
for i in range(1, N+1):
    print(' '*(N-i),end='')
    print('*'*i)