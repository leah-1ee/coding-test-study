lst=list(map(int, input().split()))
count=[0]*10

for i in lst:
    if i==0:
        break

    k=i//10
    count[k]+=1

for i in range(1,10):
    print(f"{i} - {count[i]}")