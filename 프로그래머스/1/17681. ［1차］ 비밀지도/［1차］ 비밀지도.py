# n x n
# 0(공백) or 1(#)
# arr1, arr2에서 모두 공백이어야 공백(0)
# 이진수 -> 10진수로 암호화 
# 공백, # 구성 문자열 배열 출력 

# 10진수 -> 2진수 문자열
def from_decimal(num):
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2
    return binary


def solution(n, arr1, arr2):
    # 정답 배열 
    answer = []
    
    # 암호 해독 
    for i in range(n):
        # 10진수 암호화 -> 2진수 
        binary1 = from_decimal(arr1[i]).zfill(n)
        binary2 = from_decimal(arr2[i]).zfill(n)
        secret_code = ''
        
        # 공통으로 0 -> 공백, 아니면 벽(#)
        for j in range(n):
            if binary1[j] == '0' and binary2[j] == '0':
                secret_code += ' '
            else:
                secret_code += '#'
        answer.append(secret_code)
    
    return answer