num=list(map(int, input().split()))
result=[]
l=0

for i in num:
    if (i==0):
        break
    result.append(i)
    l += 1

hap=sum(result)
cul = hap/l

print(f"{hap} {cul:.1f}")