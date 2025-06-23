n = int(input())
arr = [input() for _ in range(n)]
alp = input()

total = 0

matches = [word for word in arr if word[0] == alp]
print(len(matches), end = " ")

for word in matches:
    total += len(word)

avr = round(total/len(matches), 2)
print(f"{avr:.2f}")