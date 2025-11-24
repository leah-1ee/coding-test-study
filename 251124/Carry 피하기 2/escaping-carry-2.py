n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
# 최댓값 저장할 변수 
max_num = -1

# carry 발생하지 않는 수 고르기 
# 처음 두 수 pick 
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            n1, n2, n3 = arr[i], arr[j], arr[k]
            # 최대 자릿수 체크 
            large = max(len(str(n1)), len(str(n2)), len(str(n3)))
            # 최대 자릿수만큼 반복: 각 자리 더해서 carry 발생 여부 검증 
            for p in range(large):
                if (n1 % 10) + (n2 % 10) + (n3 % 10) >= 10:
                    break 
                else: 
                    n1 //= 10 
                    n2 //= 10
                    n3 //= 10
            # 모든 자릿수에서 carry 발생하지 않으면 
            else:
                max_num = max(max_num, arr[i] + arr[j] + arr[k])

print(max_num)      

