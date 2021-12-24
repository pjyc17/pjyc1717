while 1:
    n = int(input())
    if n == -1:
        break
    ans = 0
    lst = []
    for i in range(1,n):
        if n % i == 0:
            ans += i
            lst.append(i)
    if ans == n:
        print(ans, end=' = ')
        for i in range(len(lst)-1):
            print(lst[i], end=' + ')
        print(lst[-1])
    else:
        print(f'{n} is NOT perfect.')