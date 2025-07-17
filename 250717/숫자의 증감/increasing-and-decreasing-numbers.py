c,a = input().split()

a = int(a)

if (c=="A"):
    for i in range(1, a+1, +1):
        print(i, end=" ")
else:
    for i in range(a, 0, -1):
        print(i, end=" ")