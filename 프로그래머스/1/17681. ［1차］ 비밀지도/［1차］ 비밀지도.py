# n x n
# 0(공백) or 1(#)
# arr1, arr2에서 모두 공백이어야 공백(0)
# 이진수 -> 10진수로 암호화 
# 공백, # 구성 문자열 배열 출력 


def solution(n, arr1, arr2):
    # 정답 배열 
    answer = []
    
    for i in range(n):
        # 비트 연산으로 지도 합치기
        merged_map = arr1[i] | arr2[i]

        # 2진수 문자열로 변환, 0b 접두어 자르기, n자리수 맞추기 
        binary_str = bin(merged_map)[2:].zfill(n)

        # 0 -> 공백, 1 -> #으로 교체
        decoded_line = binary_str.replace('0', ' ').replace('1', '#')

        answer.append(decoded_line)
    
    return answer