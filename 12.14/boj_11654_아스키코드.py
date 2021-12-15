n = input()
if '0' <= n <= '9' or 'A' <= n <= 'Z' or 'a' <= n <= 'z':
    print(ord(n))       
##########################################################
a = input()
def sol(a):
    try:
        return chr(a)
    except:
        return ord(a)
print(sol(a))