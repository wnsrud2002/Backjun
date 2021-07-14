N = int(input())
N_1 = N
count = 0

while(1):
    a = N//10 + N%10
    b = (N%10)*10 + (a%10)
    N = b
    count += 1
    if (N == N_1):
        break
print(count)
    
