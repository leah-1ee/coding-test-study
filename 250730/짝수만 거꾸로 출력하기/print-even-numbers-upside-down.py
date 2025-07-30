num=int(input())
n=list(map(int, input().split()))
result=[]

for i in n:
    if i%2==0:
        result.append(i)

for j in reversed(result):
    print(j, end=" ")