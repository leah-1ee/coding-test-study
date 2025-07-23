n = int(input())
k=11

for i in range(1, n+1):
    for j in range(n):
        print(k, end=" ")
        k += 2
    k = 11
    k += 2*i


    print()