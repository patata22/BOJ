v='aeiou'

for _ in range(int(input())):
    count=0
    name=input()
    print(name)
    l=len(name)
    for x in name:
        if  x in v:count+=1
    if count*2>l:print(1) 
    else:print(0)