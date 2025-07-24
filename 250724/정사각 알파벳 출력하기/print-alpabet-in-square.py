n = int(input())
k=0

for i in range(n):
    for j in range(n):
        print(chr(65+k), end="")
        k+=1
    print()