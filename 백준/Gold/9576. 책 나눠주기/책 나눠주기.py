import sys
input=sys.stdin.readline

for tt in range(int(input())):
    n,m=map(int,input().split())
    student=[tuple(map(int,input().split())) for i in range(m)]
    student.sort(key= lambda x: x[1])
    used=[0]*(n+1)
    answer=0
    for a,b in student:
        for i in range(a,b+1):
            if not used[i]:
                used[i]=1
                answer+=1
                break
            
    print(answer)
