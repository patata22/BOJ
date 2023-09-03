temp=[]
for x in input():
    if 48<=ord(x)<=57: continue
    temp.append(x)
temp=''.join(temp)
print(1) if input() in temp else print(0)
