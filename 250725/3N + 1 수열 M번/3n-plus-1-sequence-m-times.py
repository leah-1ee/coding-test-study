m=int(input())
count = 0 

for _ in range(m):
    n=int(input())

    while (n!=1):
        if (n%2==0):
            n /= 2
        else:
            n=n*3+1
        count += 1

    print(count)
    count = 0
    