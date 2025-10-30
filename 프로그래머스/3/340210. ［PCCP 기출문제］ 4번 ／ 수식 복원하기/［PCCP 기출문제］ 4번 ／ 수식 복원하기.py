def to_decimal(n_str, base):
    """주어진 진법(base)의 문자열 n_str을 10진법 정수로 변환"""
    # 진법에 맞지 않는 문자(예: 8진법에서 8이나 9)가 있으면 오류 발생
    try:
        return int(n_str, base)
    except ValueError:
        return None

def from_decimal(n_dec, base):
    """10진법 정수 n_dec을 주어진 진법(base)의 문자열로 변환"""
    if n_dec == 0:
        return "0"
    
    result = ""
    while n_dec > 0:
        result = str(n_dec % base) + result
        n_dec //= base
    return result

def check_base(exp, base):
    """주어진 진법(base)에서 수식 exp가 성립하는지 확인"""
    A_str, op, B_str, eq, C_str = exp.split()
    
    # 1. 진법 유효성 확인: base보다 크거나 같은 숫자가 있는지 확인 (int(n_str, base)가 처리하지 못하는 경우 대비)
    max_digit = 0
    for s in [A_str, B_str, C_str]:
        for char in s:
            max_digit = max(max_digit, int(char))
    
    if max_digit >= base:
        return False
        
    # 2. 10진법으로 변환 및 수식 성립 여부 확인
    A_dec = to_decimal(A_str, base)
    B_dec = to_decimal(B_str, base)
    C_dec = to_decimal(C_str, base)
    
    if op == '+':
        return A_dec + B_dec == C_dec
    elif op == '-':
        return A_dec - B_dec == C_dec
    return False

def solve_expression(A_str, op, B_str, base):
    """주어진 진법(base)으로 수식의 10진법 결과와 base진법 문자열 결과를 반환"""
    A_dec = to_decimal(A_str, base)
    B_dec = to_decimal(B_str, base)
    
    if A_dec is None or B_dec is None:
        return None, None
        
    if op == '+':
        result_dec = A_dec + B_dec
    else: # op == '-'
        result_dec = A_dec - B_dec

    # 진법에 맞지 않는 숫자가 입력되었을 경우를 대비하여 None 체크
    if result_dec < 0:
        return None, None
        
    result_str = from_decimal(result_dec, base)
    return result_dec, result_str

def solution(expressions):
    
    # 1. 가능한 진법 범위 찾기 (최소 진법 결정)
    min_base_required = 2 
    for exp in expressions:
        A_str, op, B_str, eq, C_str = exp.split()
        for s in [A_str, B_str, C_str]:
            if s != 'X':
                for char in s:
                    min_base_required = max(min_base_required, int(char) + 1)
                    
    # 2. 유효한 진법 리스트 (확정된 수식을 기반으로 검증)
    valid_bases = []
    for base in range(min_base_required, 10): 
        is_valid = True
        for exp in expressions:
            if 'X' not in exp:
                if not check_base(exp, base):
                    is_valid = False
                    break
        
        if is_valid:
            valid_bases.append(base)

    # 3. 'X' 수식 결과 채우기
    results = []
    
    for exp in expressions:
        if 'X' not in exp:
            continue

        A_str, op, B_str, eq, C_str = exp.split()
        
        # 3-1. 모든 유효 진법으로 결과를 시뮬레이션
        possible_results_str = set() # ✨핵심 수정: 결과 문자열만을 저장하여 종류를 카운트
        
        for base in valid_bases:
            result_dec, result_str = solve_expression(A_str, op, B_str, base)
            
            # 결과 문자열에 base보다 크거나 같은 숫자가 있으면 안 됨
            max_result_digit = 0
            for char in result_str:
                max_result_digit = max(max_result_digit, int(char))

            if result_dec is not None and max_result_digit < base:
                possible_results_str.add(result_str) 

        # 3-2. 최종 결괏값 결정
        
        # Case 1: 결과 표기법의 종류가 2개 이상일 때 (불확실)
        if len(possible_results_str) > 1:
            final_str = '?'
            
        # Case 2: 결과 표기법이 유일할 때 (확정)
        elif len(possible_results_str) == 1:
            final_str = possible_results_str.pop()
            
        # Case 3: 유효 진법이 없어 결과를 계산하지 못한 경우 (불확실)
        else: 
            final_str = '?' 
            
        # 3-3. 결과 문자열 생성
        result_exp = f"{A_str} {op} {B_str} = {final_str}"
        results.append(result_exp)

    return results