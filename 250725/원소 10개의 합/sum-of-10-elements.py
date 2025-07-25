arr = list(map(int, input().split()))

s = 0

for i in range(10):
    s += arr[i]
print(s)