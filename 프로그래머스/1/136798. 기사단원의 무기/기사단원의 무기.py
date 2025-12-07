# 기본: num의 약수의 개수
# 약수의 개수 > limit -> power 

def solution(number, limit, power):
    answer = 0
    
    # 모든 번호 순회 
    for i in range(1, number+1):
    
        # 약수의 개수
        cnt = 0

        # 약수의 개수 세기: 제곱근까지만 반복 
        for j in range(1, int(i ** 0.5) + 1):
            # 약수 쌍 더하기
            if i % j == 0:
                cnt += 2

                # 제곱근이면 중복 제거(-1)
                if j ** 2 == i:
                    cnt -= 1
            
            # limit 초과하면 바로 break
            if cnt > limit:
                cnt = power
                break

        answer += cnt  
    
    
    return answer