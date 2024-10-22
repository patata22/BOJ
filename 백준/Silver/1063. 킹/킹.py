dx=(-1,-1,-1,0,0,1,1,1)
dy=(-1,0,1,-1,1,-1,0,1)
D={}
temp=['LB','B','RB','L','R','LT','T','RT']
for i in range(8):
    D[temp[i]]=i
A,B,n=input().split()
y=ord(A[0])-65
x=int(A[1])-1
sy=ord(B[0])-65
sx=int(B[1])-1
n=int(n)
for _ in range(n):
    d=D[input()]
    if not (0<=x+dx[d]<8 and 0<=y+dy[d]<8): continue
    if x+dx[d]==sx and y+dy[d]==sy:
        if not (0<=sx+dx[d]<8 and 0<=sy+dy[d]<8): continue
        sx+=dx[d]
        sy+=dy[d]
    x+=dx[d]
    y+=dy[d]
    
print(chr(y+65)+str(x+1))
print(chr(sy+65)+str(sx+1))