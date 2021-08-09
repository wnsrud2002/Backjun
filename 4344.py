a = int(input())

for i in range(a):
    num = list(map(int, input().split()))
    avg = (sum(num) - num[0])/num[0]
    cnt = 0

    for j in range(1, num[0]+1):
        if num[j] > avg:
            cnt += 1
    
    print("{:.3f}%".format(cnt/num[0]*100))
