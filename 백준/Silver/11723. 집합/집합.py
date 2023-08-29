import sys
input=sys.stdin.readline

S=[0]*21

for _ in range(int(input())):
    temp=input().split()
    c=temp[0]
    if c=='all': S=[1]*21
    elif c=='empty': S=[0]*21
    else:
        x=int(temp[1])
        if c=='add': S[x]=1
        elif c=='remove': S[x]=0
        elif c=='check':  print(S[x])
        elif c=='toggle': S[x]=1-S[x]