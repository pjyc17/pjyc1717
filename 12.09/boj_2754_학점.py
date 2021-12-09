chr = input()
ans = 0.0
def bb():
    global ans
    if len(chr) == 2:
        if chr[1] == '+':
            ans += 0.3
        elif chr[1] == '0':
            ans += 0
        elif chr[1] == '-':
            ans -= 0.3
        else:
            return ans
def ff():
    global ans
    if chr[0] == 'A':
        ans += 4.0
    elif chr[0] == 'B':
        ans += 3.0
    elif chr[0] == 'C':
        ans += 2.0
    elif chr[0] == 'D':
        ans += 1.0
    else: 
        return ans
ff()
bb()
print(ans)
# A+: 4.3, A0: 4.0, A-: 3.7

# B+: 3.3, B0: 3.0, B-: 2.7

# C+: 2.3, C0: 2.0, C-: 1.7

# D+: 1.3, D0: 1.0, D-: 0.7

# F: 0.0