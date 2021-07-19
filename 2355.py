a, b = map(int, input().split())
m = max(a, b)
n = min(a, b)

result = (a + b) * (m - n + 1) / 2
print(int(result))



