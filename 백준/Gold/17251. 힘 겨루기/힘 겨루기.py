n=int(input())
number=list(map(int,input().split()))
red=[0]*n
blue=[0]*n
red[0]=number[0]
for i in range(1,n):
    red[i]=max(red[i-1],number[i])
blue[-1]=number[-1]
for i in range(n-2,-1,-1):
    blue[i]=max(blue[i+1],number[i])
red.pop()
blue=blue[1:]
redwin=0
bluewin=0
for i in range(n-1):
    if red[i]>blue[i]: redwin+=1
    elif red[i]<blue[i]: bluewin+=1

if redwin>bluewin:print('R')
elif redwin<bluewin:print('B')
else: print('X') 
                
