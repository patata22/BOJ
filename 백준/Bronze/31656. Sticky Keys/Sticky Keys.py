answer=[]
before=""
for x in input():
    if x==before: continue
    before=x
    answer.append(x)
print(''.join(answer))