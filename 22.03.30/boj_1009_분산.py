for tc in range(1, 1 +int(input())):
    a, b = map(int,input().split())
    # if (a == 1):
    #     print(1)
    # elif (a == 2):
    #     print(2**(b%4)%10)
    # elif (a == 3):
    ans = a**(b%4+4)%10 
    if(ans == 0):
        print(10)
    else:
        print(ans)



# 1 > 1 
# 2 > 2 4 8 6
# 3 > 3 9 7 1
# 4 > 4 6 4 6 
# 5 > 5 5 5 5
# 6 > 6 6 6 6
# 7 > 7 9 3 1
# 8 > 8 4 2 6
# 9 > 9 1 9 1