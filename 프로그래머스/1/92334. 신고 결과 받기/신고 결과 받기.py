# 여러번 신고 ok but 1회만 카운트
# k번 이상 신고됨 -> 정지 & 신고한 유저에게 메일 알림
# 처리 결과 메일을 받은 횟수를 배열에 담아 return
# report: "신고자 신고받은유저"

"""
메일 받은 횟수 카운트.. 내가 누구한테 신고했는지 알아야되고 & 신고한 사람이 정지됐는지 알아야
정지된 사람 먼저 체크 -> 정지 리스트 만들어
한번 더 for -> 정지 리스트에 있는 사람 신고했으면 걔한테 +1
중복신고하면.,?

누구한테 신고했는지 신고 리스트 만들기
정지된 사람 체크 -> 정지 리스트
신고 리스트 set처리, 정지 리스트에 있으면 +1하고 pop
"""


def solution(id_list, report, k):
    
    user_report = {user_id:[] for user_id in id_list}
    stopped_user = {user_id:0 for user_id in id_list}
    blocked_list = []
    email = []
    
    for report_result in report:
        reporter, accused = report_result.split()
        if accused not in user_report[reporter]:
            user_report[reporter].append(accused)
            stopped_user[accused] += 1
        
    for name, num in zip(stopped_user.keys(), stopped_user.values()):
        if num >= k:
            blocked_list.append(name)
            
    for user in user_report.keys():
        email_num = 0
        for name in user_report[user]:
            if name in blocked_list:
                email_num += 1
        email.append(email_num)
    
    
    return email