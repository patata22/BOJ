import sys
input=sys.stdin.readline

n=int(input())
graph=[int(input(),2) for i in range(n)]
answer=[]

for _ in range(int(input())):
    a,b=map(int,input().split())
    a-=1
    b-=1
    answer.append((graph[a]&graph[b]).bit_count())

print(*answer,sep='\n')