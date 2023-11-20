a,b=map(int,input().split(':'))

total=3600*a+60*b-60*a-b
h=str(total//3600)
m=str(total%3600//60)
s=str(total%3600%60)
if len(h)==1:h='0'+h
if len(m)==1:m='0'+m
if len(s)==1:s='0'+s
print(h,m,s,sep=':')
