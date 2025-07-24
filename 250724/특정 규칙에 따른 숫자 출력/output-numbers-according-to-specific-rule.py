n = int(input())
k=1

for i in range(n, 0, -1):
    for j in range(n-i):
        print(" ", end=" ")

    for j in range(1, i+1):
        if (k>9):
            k=1
        print(k, end=" ")
        k+=1
    print()