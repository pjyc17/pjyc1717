#@는 3을 곱하고, %는 5를 더하며, #는 7을 빼는 연산자이다. 따라서, 화성에서는 수학 식의 가장 앞에 수가 하나 있고, 그 다음에는 연산자가 있다.
for tc in range(1, int(input())+1):
    arr = list(input().split())
    ans = float(arr[0])
    for i in range(1,len(arr)):
        if arr[i] == '@':
            ans = 3 * ans
        elif arr[i] == '%':
            ans = ans + 5
        elif arr[i] == '#':
            ans = ans - 7
    print('%0.2f' %ans)