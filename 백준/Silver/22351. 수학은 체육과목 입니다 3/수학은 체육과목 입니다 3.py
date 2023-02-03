n=input()
idx=0
now=1
temp=now
while idx<len(n):
    l=len(str(temp))
    if n[idx:idx+l]==str(temp):
        temp+=1
        idx+=l
    else:
        now+=1
        idx=0
        temp=now

print(now,temp-1)
        
