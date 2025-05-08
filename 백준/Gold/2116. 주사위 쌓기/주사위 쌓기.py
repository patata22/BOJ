import sys
input=sys.stdin.readline

def getMax(dice,top,bottom):
    result=0
    for x in dice:
        if x==top or x==bottom: continue
        result=max(result,x)
    return result

bot={0:5, 1:3, 2:4, 3:1, 4:2, 5:0}
dices=[tuple(map(int,input().split())) for i in range(int(input()))]

answer=0
for i in range(1,7):
    bottom=i
    temp=0
    for dice in dices:
        top=dice[bot[dice.index(bottom)]]
        temp+=getMax(dice,top,bottom)
        bottom=top
    answer=max(answer,temp)

print(answer)
