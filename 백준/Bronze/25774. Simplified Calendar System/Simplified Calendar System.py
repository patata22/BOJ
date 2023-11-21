d,m,y,n=map(int,input().split())
n-=1
start=360*y+30*m+d
d,m,y=map(int,input().split())
end=360*y+30*m+d
n+=end-start
print(n%7+1)
