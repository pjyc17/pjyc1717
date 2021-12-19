a, b, c = map(int, input().split())
i = 0
while 1:
    N1 = 15*i + a
    N2 = 28
    if N1 % 28 == b and N1 % 19 == c:
        print(N1)
        break
    i += 1
# E,S,M,cnt =1,1,1,1

# i_E , i_S , i_M = map(int,input().split())

# while(True):
#     if i_E==E and i_S==S and i_M==M :
#         break
#     E+=1 ; S+=1 ; M+=1; cnt+=1
#     if E>=16 : E-=15
#     if S>=29 : S-=28
#     if M>=20 : M-=19



# print(cnt)