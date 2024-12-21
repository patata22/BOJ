import sys
input=sys.stdin.readline

def seive():
    for i in range(2,1000001):
        if not prime[i]:
            for j in range(i,1000001,i):
                prime[j]=i

def sol(x):
    global oddCnt
    while x!=1:
        p=prime[x]
        oddCnt-=count[p]
        while x%p==0:
            count[p]=1-count[p]
            x//=p
        oddCnt+=count[p]
    if oddCnt: return 'NE'
    else: return 'DA'
    
prime=[0]*1000001
count=[0]*1000001
seive()
oddCnt=0

n=int(input())
answer=[]
for _ in range(n):
    answer.append(sol(int(input())))

print('\n'.join(answer))
