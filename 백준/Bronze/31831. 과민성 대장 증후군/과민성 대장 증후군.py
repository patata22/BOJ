stress=0
answer=0
n,m=map(int,input().split())
for x in map(int,input().split()):
    stress=max(0,stress+x)
    if stress>=m: answer+=1
print(answer)
