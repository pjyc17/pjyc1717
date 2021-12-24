def lst(l):
    global st
    if l == L and ('a' in st or 'e' in st or 'i' in st or 'u' in st or 'o' in st):
        print(st)
        return
    else:
        for i in range(l,C):
            if not visited[i]:
                visited[i] = 1
                st += arr[i]
                lst(l+1)
                st.remove(arr[i])
                visited[i] = 0

L, C = map(int, input().split())
arr = list(input().split())
visited = [0]*C
s = []
st = []
arr.sort()

for i in range(C):
    if arr[i] in ['a','e','i','o','u']:
        s.append(i)
lst(0)

'''
4 6
a t c i s w4 6
a t c i s w
'''
