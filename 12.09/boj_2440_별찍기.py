N = int(input())
for i in range(N):
    print(' '*(i),end='')
    print('*'*(2*(N-i)-1))
    # print(' '*(i+1))
for i in range(N-1,0,-1):
    print(' '*(i-1), end='')
    print('*'*(2*(N-i+1)-1))
    # print(' '*(i))