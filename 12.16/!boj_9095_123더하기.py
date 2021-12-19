for tc in range(1,int(input())+1):
    n = int(input())
    lst = [0 for _ in range(n)]
    flag = 0
    cnt = 0
    
    for j in range(n):
        for i in range(3, 0):
            if lst[j] == 0:
                lst[j] += i
            else: break

            if sum(lst) == n:
                print(lst)
                cnt += 1
                flag = 1
                break
            else:
                continue
        if flag == 1:
            break
