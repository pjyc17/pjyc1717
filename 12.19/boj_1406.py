from sys import stdin 
st = stdin.readline().strip() 
n = int(input()) 
cursor = len(st) 
for line in stdin: 
    if line[0] == 'L': 
        if not cursor == 0: 
            cursor -= 1 
        else: 
            continue 
    elif line[0] == 'D': 
        if not cursor == len(st): 
            cursor += 1 
        else: 
            continue 
    elif line[0] == 'B': 
        if not cursor == 0: 
            st = st[0:cursor-1] + st[cursor:] 
        else: 
            continue 
    elif line[0] == 'P': 
        st = st[0:cursor-1] + line[2] + st[cursor:] 
print(st)
