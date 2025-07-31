lst=list(map(int, input().split()))
count=[0]*11

for i in lst:
    if i==0:
        break
    k=i//10
    count[k]+=1

for i in range(10, 0, -1):
    print(f"{i}0 - {count[i]}")