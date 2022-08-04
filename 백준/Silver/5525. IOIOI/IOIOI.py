n=int(input())
s=int(input())
m=input()

idx= 0
answer=0
while idx<s-2:
    if m[idx]=='I':
        temp=0
        while idx<s-2:
            if m[idx+1]=='O' and m[idx+2]=='I':
                temp+=1
                idx+=2
            else:
                idx+=1
                break
            
        if temp>=n:answer+= temp-n+1
        
    else: idx+=1
print(answer)
    
