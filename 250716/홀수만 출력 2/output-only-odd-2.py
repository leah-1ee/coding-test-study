b, a = map(int, input().split())

for i in range(b, a-1, -2):
    if (b%2==0):
        b -= 1

    print(i, end=" ")
    