lst=list(map(int, input().split()))
count=[0]*10

for i in lst:
    count[i]+=1

for i in range(1, 7):
    print(f"{i} - {count[i]}")
