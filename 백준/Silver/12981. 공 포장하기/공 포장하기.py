r,g,b=map(int,input().split())
answer=0

temp=min(r,g,b)
answer+=temp
r-=temp
g-=temp
b-=temp

answer+=r//3
r%=3
answer+=g//3
g%=3
answer+=b//3
b%=3

temp=min(r,g)
answer+=temp
r-=temp
g-=temp

temp=min(g,b)
answer+=temp
b-=temp
g-=temp

temp=min(r,b)
answer+=temp
r-=temp
b-=temp

answer+=r//2
answer+=r%2
answer+=g//2
answer+=g%2
answer+=b//2
answer+=b%2

print(answer)
