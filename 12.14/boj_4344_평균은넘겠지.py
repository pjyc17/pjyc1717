for tc in range(1, int(input())+1):
    arr = list(map(int,input().split()))
    cnt = 0
    sum_ = 0
    for i in range(1, len(arr)):
        sum_ += arr[i]
    avg_ = sum_ / (len(arr)-1)

    for i in range(1,len(arr)):
        if avg_ < arr[i]:
            cnt += 1
    print('{:.3f}%'.format(cnt / (len(arr)-1)*100))
