while True:
    lst = list(map(int,input().split()))

    if lst == [0, 0, 0]:
        break
    else:
        lst.sort()
        if lst[0]**2 + lst[1]**2 == lst[2]**2:
            print('right')
        else:
            print('wrong')