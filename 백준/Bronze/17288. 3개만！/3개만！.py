x=input()

answer=0

now=x[0]
count=1
for i in range(1,len(x)):
    if ord(x[i])==ord(now)+1:
        count+=1
    else:
        if count==3:answer+=1
        count=1
    now=x[i]
if count==3:answer+=1

print(answer)
            
        
        
