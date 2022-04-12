n = int(input())
cnt = 0
letter = 666
while True:
    if '666' in str(letter):
        cnt += 1
    if cnt == n:
        print(letter)
        break
    letter += 1

print(type(n))