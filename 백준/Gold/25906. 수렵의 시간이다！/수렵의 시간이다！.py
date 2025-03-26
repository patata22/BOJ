def choice1(money):
    choice2(money)
    for i in range(m1):
        if cost1[i]<=money:
            for j in range(5): level[j]+=skill1[i][j]
            choice2(money-cost1[i])
            for j in range(5): level[j]-=skill1[i][j]
                
def choice2(money):
    choice3(money)
    for i in range(m2):
        if cost2[i]<=money:
            for j in range(5): level[j]+=skill2[i][j]
            choice3(money-cost2[i])
            for j in range(5): level[j]-=skill2[i][j]

def choice3(money):
    choice4(money)
    for i in range(m3):
        if cost3[i]<=money:
            for j in range(5): level[j]+=skill3[i][j]
            choice4(money-cost3[i])
            for j in range(5): level[j]-=skill3[i][j]

def choice4(money):
    calc()
    if money>=k:
        for i in range(5):
            if level[i]:
                level[i]-=1
                for j in range(5):
                    if i==j: continue
                    level[j]+=1
                    calc()
                    level[j]-=1
                level[i]+=1

def calc():
    global answer
    result=0
    for i in range(5):
        if not level[i]: continue
        now=min(level[i],maxLevel[i])-1
        result+=damage[i][now]
    answer=max(answer,result)
    
t,k=map(int,input().split())

maxLevel=[]
damage=[]
inventory=[-1]*3
for _ in range(5):
    temp=list(map(int,input().split()))
    maxLevel.append(temp[0])
    damage.append(temp[1:])

level=[0]*5

m1=int(input())
cost1=list(map(int,input().split()))
skill1=[list(map(int,input().split())) for i in range(m1)]
m2=int(input())
cost2=list(map(int,input().split()))
skill2=[list(map(int,input().split())) for i in range(m2)]
m3=int(input())
cost3=list(map(int,input().split()))
skill3=[list(map(int,input().split())) for i in range(m3)]

answer=0

choice1(t)

print(answer)