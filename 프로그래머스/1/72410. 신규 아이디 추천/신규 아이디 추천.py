def solution(new_id):
    
    # 1. 모든 대문자를 소문자로 치환
    new_id = new_id.lower()
    
    # 2. 허용되지 않는 문자 제외
    for char in new_id:
        if char.isalpha() or char.isdigit():
            continue
        elif char in ['-', '_', '.']:
            continue
        else:
            new_id = new_id.replace(char, '')
   
    # 3. 연속 마침표 -> 단일 마침표
    while('..' in new_id):
        new_id = new_id.replace('..', '.')
               
    # 4. 마침표가 처음이나 끝에 위치하면 제거
    if new_id and new_id[0] == '.':
        new_id = new_id[1:]
        
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]

    # 5. 빈 문자열이면 a 대입
    if not new_id:
        new_id = 'a'
    
    # 6. 길이 16 이상: 앞 15개 문자만 살리기
    if len(new_id) >= 16:
        new_id = new_id[:15]
    
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    
    # 7. 길이 2 이하: 길이 3까지 마지막 문자 반복
    while(len(new_id) <= 2):
        new_id += new_id[-1]
    
    return new_id