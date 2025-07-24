n = int(input())
k=0

for i in range(n):
    
    if (i%2==0):
        for j in range(n):
            k+=1
            print(k, end=" ")
    else:
        for j in range(n):
            k+=2
            print(k, end=" ")
    print()