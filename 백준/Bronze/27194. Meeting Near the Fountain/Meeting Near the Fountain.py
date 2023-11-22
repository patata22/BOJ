n,t=map(int,input().split())
t*=60
m=int(input())
x,y=map(int,input().split())
answer=m/x+(n-m)/y
if answer<=t: print(0)
else:
    answer-=t
    A=int(answer//60)
    if answer%60: A+=1
    print(A)
   