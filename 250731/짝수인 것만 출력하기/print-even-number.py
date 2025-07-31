n=int(input())
result=[]
lst=list(map(int, input().split()))

for i in lst:
    if i%2==0:
        result.append(i)
for j in result:
    print(j, end=" ")