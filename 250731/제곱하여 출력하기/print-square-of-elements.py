n=int(input())

lst=list(map(int, input().split()))

answer=[i*i for i in lst]

for k in answer:
    print(k, end=" ")