a, b = map(int, input().split())

for i in range(a, b+1, 2):
    if (a%2 == 0):
        a += 1
    print(i, end=" ")