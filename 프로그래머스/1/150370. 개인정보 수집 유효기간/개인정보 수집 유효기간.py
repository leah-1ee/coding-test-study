# 파기해야 할 개인정보의 번호를 오름차순

def solution(today, terms, privacies):
    answer = []
    
    # 유효기간 딕셔너리 
    terms_dict = {}
    for term in terms:
        alp, month = term.split()
        terms_dict[alp] = int(month)
    
    # 오늘 날짜 분리 
    t_year, t_month, t_day = map(int, today.split('.'))
       
    for i, privacy in enumerate(privacies):
        # 가입 날짜 분리 
        date, term = privacy.split()
        year, month, day = map(int, date.split('.'))
        
        # 가입 날짜 + 유효기간 
        month += terms_dict[term]
        year += month // 12
        month %= 12
        day -= 1
        
        if day < 1:
            month -= 1
            day += 28
            
        if month < 1:
            year -= 1
            month += 12

        # 유효기간이 지났으면 파기 대상 
        if (year < t_year)\
        or (year == t_year) and month < t_month\
        or (year == t_year) and (month == t_month) and (day < t_day):
            answer.append(i+1)
            
          
    return answer