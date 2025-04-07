from collections import deque

direct=((),(0,1,3,4), (0,1,2), (1,2,4,5), (0,3,6), (1,3,4,5,7), (2,5,8), (3,4,6,7), (6,7,8),(4,5,7,8))

def visitCheck(node,idx):
    a,b,c,d,e,f,g,h,i=node
    if not visited[a][b][c][d][e][f][g][h][i]:
        visited[a][b][c][d][e][f][g][h][i]=1
        track[a][b][c][d][e][f][g][h][i]=idx
        return False
    return True

def makeNxt(node,idx):
    result=node[:]
    for x in direct[idx]:
        result[x]=(result[x]+1)%4
    return result

def makePrev(node,idx):
    result=node[:]
    for x in direct[idx]:
        result[x]=(result[x]-1)%4
    return result

def getTrack(a,b,c,d,e,f,g,h,i):
    return track[a][b][c][d][e][f][g][h][i]

def sol():
    q=deque()
    q.append(start)
    visitCheck(start,0)
    while q:
        now=q.popleft()
        for i in range(1,10):
            nxt=makeNxt(now,i)
            if not visitCheck(nxt,i):q.append(nxt)
                
    result=[]
    a,b,c,d,e,f,g,h,i = [0]*9
    idx = getTrack(a,b,c,d,e,f,g,h,i)
    while idx!=0:
        result.append(idx)
        a,b,c,d,e,f,g,h,i=makePrev([a,b,c,d,e,f,g,h,i],idx)
        idx=getTrack(a,b,c,d,e,f,g,h,i)
        
    return sorted(result)

start=[0]*9
for i in range(3):
    temp=list(map(int,input().split()))
    for j in range(3):
        start[3*i+j]=temp[j]

visited=[[[[[[[[[0]*4 for i in range(4)] for i in range(4)] for i in range(4)] for i in range(4)] for i in range(4)] for i in range(4)] for i in range(4)] for i in range(4)]
track=[[[[[[[[[0]*4 for i in range(4)] for i in range(4)] for i in range(4)] for i in range(4)] for i in range(4)] for i in range(4)] for i in range(4)] for i in range(4)]

print(*sol())
