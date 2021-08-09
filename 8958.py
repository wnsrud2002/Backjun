a = int(input())

for i in range(a):
    b = input()
    c = list(b)

    s = 0
    count = 1

    for i in c:
        if i == 'O':
            s += count
            count += 1
        else:
            count = 1

    print(s)
