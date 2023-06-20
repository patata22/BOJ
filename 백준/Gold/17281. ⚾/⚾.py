from collections import deque

def playball():
    score=0
    linenumber=0
    def playInning(i):
        nonlocal linenumber
        outCount=0
        score=0
        base=[0,0,0,0]
        while outCount<3:
            result=number[i][lineup[linenumber]]
            linenumber=(linenumber+1)%9
            if result==0:
                outCount+=1
            else:
                if result==1:
                    score+=base[3]
                    base[3],base[2]=base[2],base[1]
                    base[1]=1
                elif result==2:   
                    score+=base[2]+base[3]
                    base[3]=base[1]
                    base[1]=0
                    base[2]=1
                elif result==3:
                    score+=base[1]+base[2]+base[3]
                    base[1]=0
                    base[2]=0
                    base[3]=1
                elif result==4:
                    score+=base[1]+base[2]+base[3]+1
                    base=[0,0,0,0]
        return score
    for i in range(n):
        score+=playInning(i)
    return score

def choice(depth):
    global answer
    if depth==9:
        answer=max(answer,playball())
        return
    elif depth==3:
        lineup.append(0)
        choice(depth+1)
        lineup.pop()
    else:
        for i in range(9):
            if not used[i]:
                used[i]=1
                lineup.append(i)
                choice(depth+1)
                lineup.pop()
                used[i]=0
    
n=int(input())

number=[tuple(map(int,input().split())) for i in range(n)]
used=[0]*9
used[0]=1
lineup=[]
answer=0

choice(0)

print(answer)