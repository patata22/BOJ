tri = []
i=0
while True:
    i+=1
    temp = (i*(i+1))//2
    if temp>1000: break
    tri.append(temp)
sumset=set()
for x in tri:
    for y in tri:
        for z in tri:
            sumset.add(x+y+z)

for _ in range(int(input())):
    print(int(int(input()) in sumset))
