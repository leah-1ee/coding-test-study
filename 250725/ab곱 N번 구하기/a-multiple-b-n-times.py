n = int(input())
s=1

for i in range(n):
    a, b = map(int, input().split())

    for j in range(a, b+1):
        s *= j

    print(s)
    s=1
    
