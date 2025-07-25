start, end = map(int, input().split())
c = 0
s = 0

for i in range(start, end+1):
    for j in range(1, i+1):
        if (i%j==0):
            c += 1
    if (c == 3):
        s += 1
    c = 0
print(s)


