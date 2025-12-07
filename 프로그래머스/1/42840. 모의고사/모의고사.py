def solution(answers):
    answer = []
    
    n = (len(answers) // 5) 
    
    person1 = ([1,2,3,4,5] * (len(answers) // 5 + 1))[:len(answers)]
    person2 = ([2, 1, 2, 3, 2, 4, 2, 5] * (len(answers) // 8 + 1))[:len(answers)]
    person3 = ([3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers) // 10 + 1))[:len(answers)]
    
    cnt1, cnt2, cnt3 = 0,0,0
    for i in range(len(answers)):
        
        
        if person1[i] == answers[i]:
            cnt1 += 1
        if person2[i] == answers[i]:
            cnt2 += 1
        if person3[i] == answers[i]:
            cnt3 += 1
        
      
    max_val = max(cnt1, cnt2, cnt3)
    
    if max_val == cnt1:
            answer.append(1)
    if max_val == cnt2:
            answer.append(2)
    if max_val == cnt3:
            answer.append(3)

    return sorted(answer)