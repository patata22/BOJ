import sys
input=sys.stdin.readline
n=int(input())

def calc(A,B,C):
    total=0
    total+=A[2]+B[2]+C[2]
    total+=one[A[0]][B[0]]+two[A[1]][B[1]]
    total+=one[B[0]][C[0]]+two[B[1]][C[1]]
    total+=one[C[0]][A[0]]+two[C[1]][A[1]]
    return total 

one=[tuple(map(int,input().split())) for i in range(10)]
two=[tuple(map(int,input().split())) for i in range(12)]

record=[[[0]*6 for i in range(12)] for i in range(10)]

for _ in range(n):
    a,b=input().rstrip().split()
    score=int(a)
    O=int(b[0])
    S=ord(b[1])-65
    record[O][S][score]+=1

final=[]
for i in range(10):
    for j in range(12):
        for k in range(1,6):
            for _ in range(min(3,record[i][j][k])):
                final.append((i,j,k))

n=len(final)
answer=0
for i in range(n):
    A=final[i]
    for j in range(i+1,n):
        B=final[j]
        for k in range(j+1,n):
            C=final[k]
            answer=max(answer,calc(A,B,C))

print(answer)
