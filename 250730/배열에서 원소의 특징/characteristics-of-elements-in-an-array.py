lst=list(map(int, input().split()))
result=[]

for i in lst:
    if i%3==0:
        break
    result.append(i)

print(result[-1])