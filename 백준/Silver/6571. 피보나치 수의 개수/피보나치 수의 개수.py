limit=(10**100)+1

pibo=[1,2]
x,y=2,1
while x+y<=limit:
    x,y=x+y,x
    pibo.append(x)

while True:
    a,b=map(int,input().split())
    if not a and not b: break
    answer=0
    for x in pibo:
        if a<=x<=b: answer+=1    
    print(answer)
