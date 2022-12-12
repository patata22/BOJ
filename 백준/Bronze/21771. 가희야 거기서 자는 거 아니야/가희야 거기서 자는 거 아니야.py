r,c=map(int,input().split())
rg,rp,cg,cp = map(int,input().split())
pillow = cg*cp
dog = rg*rp

p=0
g=0
for i in range(r):
    temp=input()
    p+=temp.count('P')
    g+=temp.count('G')

if g==dog and pillow!=p:print(1)
else: print(0)
    
