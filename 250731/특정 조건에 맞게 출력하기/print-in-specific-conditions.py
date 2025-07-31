n=list(map(int, input().split()))
lst=[]

for i in n:
    if i==0:
        break
    elif i%2==0:
        lst.append(i/2)
    else:
        lst.append(i+3)

for j in lst:
    print(int(j), end=" ")