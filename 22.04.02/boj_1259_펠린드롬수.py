while True:
    a = input()
    cnt = 0
    if a == '0':
        break
    for i in range(len(a)//2):
        if a[i] != a[len(a) - 1 - i]:
            break
        else:
            cnt += 1

    if cnt == len(a) // 2:
        print('yes')
    else:
        print('no')
        

