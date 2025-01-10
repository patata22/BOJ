n=int(input())

def sol(idx):
    global total,cnt
    MUL = 10**(n-1-(idx//4))
    cand=set([0,1,2,3,4,5,6,7,8,9])
    for x in range(5):
        for y in range(idx,idx+3):
            if board[x][y]=='#':
                cand-=target[x][y-idx]
    cnt*=len(cand)
    temp=[len(cand),0]
    for x in cand:
        temp[1]+=MUL*x
    return temp
                


target=[]
target.append([set([1]),set([1,4]),set()])
target.append([set([1,2,3,7]), set([0,1,2,3,4,5,6,7,8,9]), set([5,6])])
target.append([set([1,7]),set([0,1,7]),set()])
target.append([set([1,3,4,5,7,9]), set([0,1,2,3,4,5,6,7,8,9]), set([2])])
target.append([set([1,4,7]),set([1,4,7]), set()])


board=[list(input()) for i in range(5)]

total=[]
cnt=1
for i in range(0,4*n,4):
    total.append(sol(i))


if not cnt: print(-1)
else:
    answer=0
    for x,y in total:
        answer+=(cnt//x)*y
    print(answer/cnt)
    
