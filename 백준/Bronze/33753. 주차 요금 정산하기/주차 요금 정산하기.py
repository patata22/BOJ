a,b,c=map(int,input().split())
t=int(input())
answer=a
if t>30:
    x,y=divmod(t-30,b)
    answer+=x*c
    if y: answer+=c
print(answer)