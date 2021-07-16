import sys
for i in range(3):
    N = int(sys.stdin.readline())
    a = []
    for k in range(N):
        a.append(int(sys.stdin.readline()))
    b = sum(a)
    if(b > 0):
        print("+")
    elif(b == 0):
        print(0)
    elif(b < 0):
        print("-")

