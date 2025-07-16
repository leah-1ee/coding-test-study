a, b = map(int, input().split())

while (a<=b):
    if (a%2!=0):
        a +=1

    print(a, end=" ")
    a += 2