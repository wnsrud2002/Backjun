m = int(input())
d = int(input())

if m == 1:
    print("Before")
if m == 2:
    if d == 18:
        print("Special")
    elif d > 18:
        print("After")
    elif d < 18:
        print("Before")
if m > 2:
    print("After")
