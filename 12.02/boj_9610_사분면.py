axis = q1 = q2 = q3 = q4 = 0
for _ in range(int(input())):
    m, n = map(int, input().split())
    if m == 0 or n == 0:
        axis += 1
    elif m > 0 and n > 0:
        q1 += 1
    elif m > 0 and n < 0:
        q4 += 1
    elif m < 0 and n < 0:
        q3 += 1
    else:
        q2 += 1
print('Q1: {}'.format(q1))
print('Q2: {}'.format(q2))
print('Q3: {}'.format(q3))
print('Q4: {}'.format(q4))
print('AXIS: {}'.format(axis))