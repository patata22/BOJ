input()
dice1=list(map(int,input().split()))
dice2=list(map(int,input().split()))
answer=0
for x in dice1:
    for y in dice2:
        if x>y: answer+=1
        elif x<y: answer-=1
if answer>0: print('first')
elif answer<0:print('second')
else: print('tie')