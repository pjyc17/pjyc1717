for tc in range(1, int(input())+1):
    chr = str(input())
    if chr == 'SUN':
        print('#{} {}'.format(tc, 7))
    elif chr == 'MON':
        print('#{} {}'.format(tc, 6))
    elif chr == 'TUE':
        print('#{} {}'.format(tc, 5))
    elif chr == 'WED':
        print('#{} {}'.format(tc, 4))
    elif chr == 'THU':
        print('#{} {}'.format(tc, 3))
    elif chr == 'FRI':
        print('#{} {}'.format(tc, 2))
    elif chr == 'SAT':
        print('#{} {}'.format(tc, 1))