n,m=map(int,input().split())

hol=[]
jjak=[]
count={}
while True:
    a,b=input().split()
    if a=='0' and b=='0': break
    a=int(a)
    if a not in count:
        count[a]=1
        if a%2==0:
            jjak.append((a,b))
        elif a%2==1:
            hol.append((a,b))
    elif a in count:
        if count[a]>=m:continue
        else:
            count[a]+=1
            if a%2==0:
                jjak.append((a,b))
            elif a%2==1:
                hol.append((a,b))
                
hol.sort(key=lambda x: (x[0],len(x[1]),x[1]))
jjak.sort(key=lambda x:(x[0],len(x[1]),x[1]))

for x in hol:print(*x)
for x in jjak:print(*x)
         
