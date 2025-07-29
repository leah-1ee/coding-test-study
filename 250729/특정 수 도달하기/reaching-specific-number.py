num=list(map(int, input().split()))
result=[]

for i in num:
    if (i>=250):
        break
    result.append(i)

s=sum(result)
l=len(result)

print(s, end=" ")
print(s/l)
    
    