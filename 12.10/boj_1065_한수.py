N = int(input())
N_ = N
cnt = 0
while N_:
    
    a = (N_)//100
    b = (N_-a*100)//10
    c = N_ % 10
    N_-= 1
    if a - b == b - c or a == 0:
        cnt += 1 
print(cnt)