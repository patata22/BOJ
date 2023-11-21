n=int(input())
turn=1
answer=[0,0]
while n:
    x,y=n//2,n//2
    if n%2: x+=1
    answer[turn]+=x
    n=y
    turn=1-turn
print(*answer)