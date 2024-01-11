import sys
input=sys.stdin.readline

change={}
reverse={}
for i in range(65,91):
    change[chr(i)]=i-65
    reverse[i-65]=chr(i)
for i in range(97,123):
    change[chr(i)]=i-71
    reverse[i-71]=chr(i)
    
distance=[[float('inf')]*52 for i in range(52)]

for _ in range(int(input())):
    a,b=map(lambda x: change[x],input().rstrip().split(' => '))
    distance[a][b]=0

for k in range(52):
    for i in range(52):
        for j in range(52):
            if distance[i][j]>distance[i][k]+distance[k][j]:
                distance[i][j]=distance[i][k]+distance[k][j]
answer=[]
for i in range(52):
    for j in range(52):
        if i==j: continue
        if distance[i][j]!=float('inf'):
            answer.append((reverse[i],reverse[j]))

print(len(answer))
for x in answer:
    print(*x,sep=' => ')
