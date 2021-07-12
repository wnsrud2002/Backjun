x = int(input())

for i in range(x):
    a,b = map(int, input().split())
    print('Case #%d: %d'%(i+1, a+b))
