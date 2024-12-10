def getValue(idx, word):
    if idx>=len(word): return 0
    if word[idx] in visited: return visited[word[idx]]
    else: return -1

def decideUp(depth,u,d,dummy):
    U=getValue(depth,up)
    if U==-1:
        for i in range(10):
            if not used[i]:
                used[i]=1
                visited[up[depth]]=i
                decideDown(depth,i,d,dummy)
                visited.pop(up[depth])
                used[i]=0
    else:
        decideDown(depth,U,d,dummy)

def decideDown(depth,u,d,dummy):
    D=getValue(depth,down)
    if D==-1:
        for i in range(10):
            if not used[i]:
                used[i]=1
                visited[down[depth]]=i
                decideResult(depth,u,i,dummy)
                visited.pop(down[depth])
                used[i]=0
    else:
        decideResult(depth,u,D,dummy)
                

def decideResult(depth,u,d,dummy):
    if depth==n:
        if dummy: return
        global answer
        answer='YES'
        return
    total=u+d+dummy
    R=getValue(depth,result)
    
    if R==-1:  
        if not used[total%10]:
            used[total%10]=1
            visited[result[depth]]=total%10
            decideUp(depth+1, 0, 0, total//10)
            visited.pop(result[depth])
            used[total%10]=0
    else:
        if R==total%10:
            decideUp(depth+1, 0, 0, total//10)
            

up,down,result=input().split()
up=list(up)[::-1]
down=list(down)[::-1]
result=list(result)[::-1]
n=max(len(up),len(down),len(result))
visited={}
used=[0]*10
answer='NO'
decideUp(0,0,0,0)
print(answer)