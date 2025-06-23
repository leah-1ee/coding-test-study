word = input()
n = int(input())

# 파이썬 뒤에서 슬라이싱하는 방법 
for elem in word[-1:-n-1:-1]:
    print(elem, end="")