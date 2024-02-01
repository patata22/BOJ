temp=input().split(':')
jump=0
answer=[]
count=0
for x in temp:
    if x: count+=1
for x in temp:
    if not x:
        if not jump:
            jump=1
            for _ in range(8-count):
                answer.append('0000')
    else:
        answer.append('0'*(4-len(x))+x)        
print(':'.join(answer))            
    
