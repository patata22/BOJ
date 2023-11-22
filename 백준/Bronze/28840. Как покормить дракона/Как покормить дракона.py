h,m=map(int,input().split(':'))
total1=60*h+m
h,m=map(int,input().split(':'))
total2=60*h+m
answer=0
if total2<=total1:total2+=1440
else:answer+=1440
answer+=total2-total1
h=str(answer//60)
m=str(answer%60)
if len(h)==1: h='0'+h
if len(m)==1: m='0'+m
print(h,m,sep=':')