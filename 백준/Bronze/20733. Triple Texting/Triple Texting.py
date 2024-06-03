x=input()
l=len(x)//3
temp=[]
for i in range(0,len(x),l):
    temp.append(x[i:i+l])
for x in temp:
    if temp.count(x)>=2:
        print(x)
        break
    
    
