
n=list(map(int, input().split()))
result=[]

for i in n:
    if (i==0):
        break
    result.append(i)

for j in reversed(result):
    print(j, end=" ")
    