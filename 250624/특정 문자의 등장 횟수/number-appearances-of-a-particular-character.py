word = input()
ee_cnt, eb_cnt = 0, 0

for i in range(len(word)-1):
    if word[i:i+2] == 'ee':
        ee_cnt += 1
    elif word[i:i+2] == 'eb':
        eb_cnt += 1

print(f"{ee_cnt} {eb_cnt}")