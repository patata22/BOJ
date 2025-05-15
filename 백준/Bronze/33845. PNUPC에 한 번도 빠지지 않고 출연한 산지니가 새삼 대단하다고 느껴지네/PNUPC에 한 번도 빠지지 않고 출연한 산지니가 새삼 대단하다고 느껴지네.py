s=set(input())
answer=[]
for x in input():
    if x in s: continue
    answer.append(x)
print(''.join(answer))
