sum_ = 0
for i in range(5):
    plus = int(input())
    if plus <= 40:
        plus = 40
        sum_ += plus
    else:
        sum_ += plus
print(sum_//5)
