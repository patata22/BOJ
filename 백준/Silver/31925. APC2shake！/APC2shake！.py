import sys
input=sys.stdin.readline

temp=[]
for _ in range(int(input())):
    name, jae,win,shake,rank=input().split()
    if jae!='jaehak': continue
    if win!='notyet': continue
    shake=int(shake)
    rank=int(rank)
    if 1<=shake<=3: continue
    temp.append((name,rank))

temp.sort(key=lambda x: x[1])
answer=[]
for i in range(min(10,len(temp))):
    
    answer.append(temp[i][0])

answer.sort()
print(len(answer))
for x in answer:print(x)
