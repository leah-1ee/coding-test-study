def solution(id_list, report, k):
    # 중복 신고 제거
    report = set(report)
    
    # 결과 담을 딕셔너리 - 이름:이메일 수
    answer = {name:0 for name in id_list}
    
    # 신고 당한 사람:신고자들
    reports = {name:[] for name in id_list}
    
    # reports 딕셔너리 작성
    for r in report:
        reporter, accused = r.split()
        reports[accused].append(reporter)
    
    # 정지 기준 넘으면 
    for accused, reporters in reports.items():
        if len(reporters) >= k:
            # 모든 신고자의 메일 카운트 +1
            for reporter in reporters:
                answer[reporter] += 1
      
    return list(answer.values())