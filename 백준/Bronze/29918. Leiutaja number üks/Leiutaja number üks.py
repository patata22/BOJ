a,b=map(int,input().split())
mine=a+10*b
other=0
for _ in range(5):
    a,b=map(int,input().split())
    other=max(other,a+10*b)
print(max(0,other-mine+1))   