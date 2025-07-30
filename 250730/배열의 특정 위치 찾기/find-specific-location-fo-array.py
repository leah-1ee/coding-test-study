st1=list(map(int, input().split()))

st2=st1[1::2]
st3=st1[2::3]

s2=sum(st2)
s3=sum(st3)/len(st3)

print(f"{s2} {s3:.1f}")