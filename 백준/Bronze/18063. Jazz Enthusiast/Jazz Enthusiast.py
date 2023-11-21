def parse(x):
    m,s=map(int,x.split(":"))
    return 60*m+s

n,c=map(int,input().split())
total=0
for _ in range(n):
    total+=parse(input())
total -= (n-1)*c
h=str(total//3600)
if len(h)==1: h='0'+h
total%=3600
m=str(total//60)
if len(m)==1: m='0'+m
s=str(total%60)
if len(s)==1: s='0'+s
print(h,m,s,sep=':')
