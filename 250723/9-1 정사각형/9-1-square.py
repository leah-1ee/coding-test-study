n = int(input())
k=9

for i in range(n):
    for j in range(n):
        print(k, end="")
        k -= 1
        if (k==0):
            k = 9
    print()