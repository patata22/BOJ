answer='No'
n=int(input())
x,y=map(int,input().split())

for _ in range(n):
    sx,sy,ex,ey=map(int,input().split())
    if sx<=x<=ex and sy<=y<=ey: answer='Yes'
print(answer)
