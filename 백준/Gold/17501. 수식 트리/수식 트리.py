import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def sol(x):
    if 1<=x<=n: return
    calc,l,r=node[x]
    multiplier[l]=multiplier[x]
    if calc=='-': multiplier[r]=-multiplier[x]
    else: multiplier[r]=multiplier[x]
    sol(l)
    sol(r)

n=int(input())

multiplier=[1]*(2*n)
posNum=[]
negNum=[]
for _ in range(n):
    x=int(input())
    if x>=0: posNum.append(x)
    else: negNum.append(x)

posNum.sort()
negNum.sort(reverse=True)
node={}

for i in range(n+1,2*n):
    temp=input().split()
    node[i] = (temp[0],int(temp[1]),int(temp[2]))

sol(2*n-1)

pos=0
neg=0

answer=0

for i in range(1,n+1):
    if multiplier[i]>=0: pos+=1
    else: neg+=1

while pos and posNum:
    answer+=posNum.pop()
    pos-=1

while neg and negNum:
    answer-=negNum.pop()
    neg-=1

if neg: answer-=sum(posNum)
elif pos: answer+=sum(negNum)

print(answer)
