n = int(input())
nums = list(map(int, input().split()))
flag = False

# Please write your code here.
# 카운트 배열 채우기 
count = [0] * (n+1)

for i in nums:
    count[i] += 1

# 뒤에서부터(큰 수부터 탐색), 중복되지 않은 수 출력
for i in range(n,-1,-1):
    if count[i] == 1:
        print(i)
        flag = True
        break

# 조건에 맞는 원소 존재하지 않음 
if flag == False:
    print("-1")
    