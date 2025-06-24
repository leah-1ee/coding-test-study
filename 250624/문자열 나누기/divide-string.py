n = int(input())
num = ''.join(input().split())


for i in range(0, len(num), 5):
    print(num[i:i+5])