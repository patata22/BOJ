n,k=input().split()

answer=0
for i in range(0,3600*(int(n)+1)):
    h=str(i//3600)
    if len(h)==1: h='0'+h
    m=str(i%3600//60)
    if len(m)==1: m='0'+m
    s=str(i%3600%60)
    if len(s)==1: s='0'+s
    if k in h or k in m or k in s: answer+=1
print(answer)
    

