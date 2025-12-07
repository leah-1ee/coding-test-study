def solution(a, b):
    
    # 월 별 날짜 수 딕셔너리 
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # 요일 저장 리스트
    # 1월 1일이 금요일이므로 나머지가 1일 때 FRI 가 나오도록 함 
    day = ['THU','FRI','SAT', 'SUN','MON','TUE','WED']

    # 1월 1일 - a월 b일 날짜 수 계산
    # a-1달 까지의 날짜 수 + b 
    total_days = sum(month[:a-1]) + b
    
    # 7로 나눈 나머지를 인덱스로 사용 
    return day[total_days % 7]
    
    