def check(x,score):
    if len(x)<l: return 0
    idx=0
    cnt=0
    for a in x:
        if idx==l:
            cnt+=1
            continue
        if a==original[idx]:idx+=1
        else: cnt+=1
        
    if idx==l: return score/cnt
    return 0

original=list(input())
l=len(original)
answer=''
gap=0
for _ in range(int(input())):
    name, score= input().split()
    now = check(name,int(score))
    if now>gap:
        gap=now
        answer=name

if not gap: print('No Jam')
else:print(answer)