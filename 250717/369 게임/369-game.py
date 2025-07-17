n = int(input())

for i in range(1, n+1):
    s = str(i)
    if ('3'in s or '6'in s or '9'in s):
        print("0", end=" ")

    elif(i%3==0):
        print("0", end=" ")

    else:
        print(i, end=" ")