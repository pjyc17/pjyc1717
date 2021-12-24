while 1:
    try:
        n = int(input())
        ans = '1'
        while 1:
            if int(ans) % n == 0:
                print(len(ans))
                break
            ans += '1'
    except EOFError:
        break
