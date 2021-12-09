for tc in range(1, int(input())+1):
    arr = []
    for univ in range(int(input())):
        u, p = map(str, input().split())
        arr.append((u,int(p)))
    max_ = 0
    for i in range(len(arr)):
        if max_ < arr[i][1]:
            max_ = arr[i][1]
            idx = i
    print(arr[idx][0])