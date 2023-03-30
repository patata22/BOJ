n,m=map(int,input().split())
answer=0
pos=[0]
neg=[0]
for x in map(int,input().split()):
    if x>0: pos.append(x)
    else: neg.append(-x)

pos.sort()
neg.sort()

for i in range(len(pos)-1,-1,-m):
    answer+=2*pos[i]
for i in range(len(neg)-1,-1,-m):
    answer+=2*neg[i]
answer-=max(pos[-1],neg[-1])
print(answer)