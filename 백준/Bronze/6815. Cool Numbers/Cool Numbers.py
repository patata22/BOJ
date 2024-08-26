square=set()
cube=set()
s,e=int(input()),int(input())
answer=0
for i in range(1,1000):
    temp=i**3
    if temp<s: continue
    if temp>e:break
    cube.add(temp)

for i in range(1,10000):
    
    temp=i**2
    if temp<s: continue
    if temp>e: break
    square.add(temp)

for x in cube:
    if x in square:answer+=1

print(answer)
