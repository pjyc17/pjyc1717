import sys
input = sys.stdin.readline
n = int(input())
ANS = 0
def sol(n):
    ans = 0
    for i in range(1,int((n)**(0.5)+1)):
        if n % i==0 and i != n**(0.5):
            ans += i
            ans += n // i
        elif i == n**(0.5):
            ans += i
    return ans
for i in range(1,n+1):
    ANS += sol(i)
print(ANS)

# import sys
# input=sys.stdin.readline

# n = int(input())

# sum_ = 0
# for i in range(1, n+1):
	# i의 배수의 개수 = i를 약수로 갖는 수
#    sum_ += (n//i)*i

# print(sum_)  