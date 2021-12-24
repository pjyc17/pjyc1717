m = int(input())

i = 2
while m > 1:
    if m % i == 0:
        print(i)
        m = m / i
    else:
        i += 1

# m = int(input())

# for i in range(2, m+1):
#     for j in range(23, 0, -1):
#         if m % (i ** j) == 0:
#             print(i)
#             m = m / i
            
# 시간초과 남

# for i in range(2, m):

