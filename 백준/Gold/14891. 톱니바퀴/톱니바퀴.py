from collections import deque

def spin(start, way):
    will_spin=[0]*4
    for i in range(start, 3):
        if gear[i][2]==gear[i+1][-2]:break
        will_spin[i+1]=1
    for i in range(start, 0,-1):
        if gear[i][-2]==gear[i-1][2]:break
        will_spin[i-1]=1
    for i in range(0,4):
        if i==start:continue
        if will_spin[i]:
            if (start-i)%2==0: gear[i].rotate(way)
            else: gear[i].rotate(-way)
    gear[start].rotate(way)

gear= [deque(map(int,(list(input())))) for i in range(4)]
for _ in range(int(input())):
    a,b=map(int,input().split())
    spin(a-1,b)
answer=0
for i in range(4):
    if gear[i][0]==1: answer+=1<<i   
print(answer)