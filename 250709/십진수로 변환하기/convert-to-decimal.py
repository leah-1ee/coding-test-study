binary = input()

# Please write your code here.
num = 0

for digit in binary:
    num = num * 2 + int(digit)

print(num)