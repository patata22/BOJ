x,y=map(int,input().split())
answer=0
while x!=y:
    answer+=1
    if y>x: x,y=y,x
    x-=y
print(answer)
    
