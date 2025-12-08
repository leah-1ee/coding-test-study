def solution(nums):

    cnt = 0        # 소수 개수
    n = len(nums)  # 주어진 숫자 수

    # 3개 수를 고르는 모든 조합 
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                # 세 수의 합
                num = nums[i] + nums[j] + nums[k]
                # 약수 있으면 break
                for l in range(2, int(num**0.5)+1):
                    if num % l == 0:
                        break
                # 약수 없으면(=소수이면) cnt +1
                else:
                    cnt += 1
                        

    return cnt