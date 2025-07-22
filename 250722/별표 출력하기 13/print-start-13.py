n = int(input())

for i in range(n*2):
    if (i%2 == 0):
        for _ in range(n-(i)//2):
            print("*", end=" ")

    else:
        for _ in range(i//2+1):
            print("*", end=" ")

    print()