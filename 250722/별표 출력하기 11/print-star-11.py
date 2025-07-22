n = int(input())

for i in range(n*2+1):
    for j in range(n*2+1):
        if (i%2 != 0) and (j%2 != 0):
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()
