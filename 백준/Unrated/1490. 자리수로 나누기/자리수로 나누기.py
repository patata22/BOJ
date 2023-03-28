from collections import deque

def gcd(x,y):
    while y: x, y = y,x%y
    return x

def getLCM(x,y):
    g=gcd(x,y)
    x//=g
    y//=g
    return g*x*y

original =input()
start=int(original)
temp = list(map(int,list(original)))
lcm=1
for x in temp:
    if x!=0:
        lcm=getLCM(lcm,x)

q=deque()
q.append(start)
while q:
    now=q.popleft()
    if not now%lcm:
        print(now)
        break
    now*=10
    for i in range(10):
        q.append(now+i)

    
            
            