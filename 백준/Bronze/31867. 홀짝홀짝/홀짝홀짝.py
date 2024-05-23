input()
odd=0
even=0
temp=list(map(int,input()))
while temp:
    if temp.pop()%2: odd+=1
    else: even+=1
if odd>even:print(1)
elif odd<even: print(0)
else:print(-1)
