n = int(input())
k = 1

for i in range(n): 
    for j in range(n):
        print(k, end="")
        k += 1
        if (k>=10):
            k=1
    print()