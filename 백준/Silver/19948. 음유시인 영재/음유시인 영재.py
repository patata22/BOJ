def sol():
    answer=[]
    if len(poet)>space+1: return -1
    for p in poet:
        before=""
        for i in range(len(p)):
            x=p[i]
            if x==before: continue
            n=ord(x.lower())-97
            count[n]-=1
            if count[n]<0: return -1
            before=x
            if i==0:
                count[n]-=1
                if count[n]<0: return -1
                answer.append(x.upper())
    return ''.join(answer)
                
        
    
    
poet=input().split()
space=int(input())
count=list(map(int,input().split()))
print(sol())

