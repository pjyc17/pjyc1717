for tc in range(1, int(input())+1):
    ans_y = ans_k = 0
    for _ in range(9):
        y, k = map(int, input().split())
        ans_y += y
        ans_k += k
    if ans_y > ans_k:
        print('Yonsei')
    elif ans_y < ans_k:
        print('Korea')
    else:
        print('Draw')