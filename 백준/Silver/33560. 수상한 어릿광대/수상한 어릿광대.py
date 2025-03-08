def play(x):
    global time,speed,bonus,score
    if time>240:init()
    if x==1:
        init()
        return
    elif x==2:
        if bonus==1: speed+=2
        else: bonus//=2
    elif x==4: time+=56
    elif x==5:
        if speed>1: speed-=1
    elif x==6:
        if bonus<32: bonus*=2
    time+=speed
    score+=bonus

def init():
    global time,speed,bonus,score
    if score>=125: answer[3]+=1
    elif score>=95: answer[2]+=1
    elif score>=65: answer[1]+=1
    elif score>=35: answer[0]+=1
    time=0
    speed=4
    bonus=1
    score=0
    
    
input()    
number=tuple(map(int,input().split()))
time=0
speed=4
bonus=1
score=0
answer=[0]*4

for x in number:play(x)

print(*answer,sep='\n')
