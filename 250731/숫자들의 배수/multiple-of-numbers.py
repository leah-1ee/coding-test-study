n=int(input())
count=0
lst=[]
i=1

while True:
    num=n*i
    lst.append(num)
    if num%5==0:
        count += 1
    if count==2:
        break
    i += 1

for j in lst:
    print(j, end=" ")

    
