m, n = map(int, input().split())
# lst = list(input() for _ in range(m))

# 0,0이 b 인가 w 인가
# 열의 갯수가 짝수인가 홀수인가 짝수이면 홀수 행과 짝수 행의 값을 비교해야하는데
# 홀수행을 검사하고 짝수행을 검사한다.

# 열의 갯수가 홀수이면 전체를 한줄로 받아와서 검사한다.
# 한줄로 받아왔을때가 편할것같은데 그거 먼저 해보자

if n % 2 == 1:
    lst = ''
    for _ in range(m):
        lst += str(input())
    print(lst[5])