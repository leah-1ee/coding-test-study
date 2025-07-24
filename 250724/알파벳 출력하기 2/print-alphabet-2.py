n = int(input())
k=0
for i in range(n, 0, -1):
    for j in range(n-i):
        print(" ", end=" ")

    for j in range(i):
        print(chr(65+k), end=" ")
        k+=1
        if (k+65>90):
            k=0
    print()