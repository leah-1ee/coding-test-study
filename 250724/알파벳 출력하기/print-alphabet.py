n = int(input())
k=0

for i in range(1, n+1):
    for j in range(i):
        print(chr(65+k), end="")
        k+=1
        if (65+k>90):
            k=0
    print()