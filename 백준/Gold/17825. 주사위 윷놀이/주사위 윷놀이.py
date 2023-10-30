
def findNext(now, count):
    if now==5:
        count-=1
        nextNode=21
    elif now==10:
        count-=1
        nextNode=25
    elif now==15:
        count-=1
        nextNode=27
    else:
        nextNode=nxt[now]
        count-=1
    while count:
        nextNode=nxt[nextNode]
        count-=1
    return nextNode
    
def sol(depth,total):
    global answer
    if depth==10:
        answer=max(answer,total)
        return
    move=dice[depth]
    for i in range(4):
        originNode = location[i]
        nextNode = findNext(originNode, move)
        if visited[nextNode]<=0:
            visited[originNode]-=1
            visited[nextNode]+=1
            location[i]=nextNode
            sol(depth+1, total+score[location[i]])
            location[i]=originNode
            visited[nextNode]-=1
            visited[originNode]+=1
        
score=[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,13,16,19,25,22,24,28,27,26,30,35,0]
nxt=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,32,22,23,24,30,26,24,28,29,24,31,20,32]
dice=list(map(int,input().split()))
location=[0,0,0,0]
visited=[0]*33
visited[-1]=-float('inf')
answer=0

sol(0,0)
print(answer)
