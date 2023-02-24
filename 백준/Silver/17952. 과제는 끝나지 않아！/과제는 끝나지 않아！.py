import sys
input=sys.stdin.readline

n=int(input())
task=[]
answer=0
for _ in range(n):
    temp=input().split()
    if temp[0]!='0':
        task.append([int(temp[1]),int(temp[2])])
    if task:
        task[-1][1]-=1
        if not task[-1][1]:
            answer+=task.pop()[0]

    
print(answer)
