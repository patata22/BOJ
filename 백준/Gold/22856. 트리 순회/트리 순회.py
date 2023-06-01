import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**7)


def sol(now):
    temp=0
    l,r=graph[now]
    if l!=-1:
        temp+=sol(l)+1
    if r!=-1:
        temp+=sol(r)+1
    return temp
def right(now,depth):
    r=graph[now][1]
    if r==-1: return depth
    else: return right(r,depth+1)
        

n=int(input())
graph=[[] for i in range(n+1)]
for _ in range(n):
    a,b,c=map(int,input().split())
    graph[a].append(b)
    graph[a].append(c)
    
answer=2*sol(1)-right(1,0)
print(answer)
