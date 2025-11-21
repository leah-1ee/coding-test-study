A = input()

# Please write your code here.
# 괄호 쌍 개수를 셀 변수 cnt 
cnt = 0

# 괄호 쌍 완전 탐색 
# (( 나오면
for i in range(len(A)-1): 
    if A[i] == '(' and A[i+1] == '(':
        # )) 있는지 확인 
        for j in range(i+2, len(A)-1):
            if A[j] == ')' and A[j+1] == ')':
                cnt += 1

print(cnt)