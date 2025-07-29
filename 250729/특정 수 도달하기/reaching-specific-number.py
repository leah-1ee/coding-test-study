num=list(map(int, input().split()))
result=[]

for i in num:
    if (i>=250):
        break
    result.append(i)

s=sum(result)
l=len(result)

print(f"{s} {s/l:.1f}")
    
    