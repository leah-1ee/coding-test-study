# 과목 수와 학점 받기 
num = int(input())
score = list(map(float, input().split()))

# 평균 학점 계산, 출력 
total = sum(score)
avr = total / num
print(f"{avr:.1f}")

# 평균 학점에 따라 출력 
if avr >= 4.0:
    print("Perfect")
elif avr < 4.0 and avr >= 3.0:
    print("Good")
else:
    print("Poor")