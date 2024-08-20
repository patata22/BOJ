a,b,h,w=map(int,input().split())

x=h//a
if h%a: x+=1
y=w//b
if w%b: y+=1
print(x*y)
