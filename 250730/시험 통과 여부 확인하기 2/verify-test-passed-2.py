num=int(input())
count=0

for i in range(num):
    n=list(map(int, input().split()))

    if(sum(n)/4 >= 60):
        print("pass")
        count+=1
    else:
        print("fail")

print(count)