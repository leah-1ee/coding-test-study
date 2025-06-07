# 학생 수 입력받기
std = int(input())
num = 0

# 학생 수만큼 반복, 점수 입력받고 평균 계산, pass/fail 출력 
for i in range(std):
    score = list(map(int, input().split()))
    avr = sum(score) / len(score)

    if avr >= 60:
        print("pass")
        num += 1
    else:
        print("fail")

# 통과한 학생 수 출력 
print(num)