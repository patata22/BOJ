a,b,c,d=map(int,input().split())
if a>b: a,b=b,a
if c>d: c,d=d,c
print(max(b,d)-min(a,c)-max(1,c-b,a-d)+2)
