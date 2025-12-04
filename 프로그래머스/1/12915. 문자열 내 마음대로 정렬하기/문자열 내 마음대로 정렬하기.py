def solution(strings, n):
        
    # strings 정렬, key: n번째 인덱스, 문자열 전체
    return sorted(strings, key = lambda x:(x[n], x))