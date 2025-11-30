N = int(input())
a, b, c = map(int, input().split())

# Please write your code here.
cnt = N ** 3

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            if (a-2 > i or i > a+2) and (b-2 > j or j > b+2) and (c-2 > k or k > c+2):
                
                cnt -= 1

print(cnt)