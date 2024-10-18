input()
cmd=input()
visited=set()
x,y=0,0
visited.add((x,y))

for c in cmd:
    if c=='S':y-=1
    elif c=='N': y+=1
    elif c=='E': x+=1
    else: x-=1
    visited.add((x,y))

print(len(visited))
