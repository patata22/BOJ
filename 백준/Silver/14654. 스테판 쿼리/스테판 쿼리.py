def getResult(idx):
    if team1[idx]-team2[idx]==1 or (team1[idx]==1 and team2[idx]==3):
        return 1
    elif team1[idx]==team2[idx]:
        return 3-win
    return 2
n=int(input())
team1=tuple(map(int,input().split()))
team2=tuple(map(int,input().split()))
win = getResult(0)
streak=1
answer=0
for i in range(1,n):
    result=getResult(i)
    if result==win:
        streak+=1
    else:
        answer=max(answer,streak)
        win=result
        streak=1
answer=max(answer,streak)
print(answer)
        
