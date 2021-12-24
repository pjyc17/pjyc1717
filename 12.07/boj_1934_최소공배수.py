for tc in range(1, int(input())+1):
    m, n = map(int, input().split())
    l = min(m, n)
    cal = 1
    # for i in range(1, l+1):
    #     if m % i == 0 and n % i == 0:
    #         cal *= i
    # print(cal)
    lst = []
    for i in range(1, m+1):
        if m % i == 0:
            lst.append(i)
    for i in range(1, n+1):
        if n % i == 0 and i not in lst:
            lst.append(i)
        # elif n % i == 0 and i in lst:
        #     lst.pop(i)
    print(lst)