n=int(input())
word=list(map(lambda x: ord(x)-97,input()))

N=len(word)
count=[0]*26
answer=0
l=0
r=-1
cnt=0

while r+1<N:
    r+=1
    if count[word[r]]==0:cnt+=1
    count[word[r]]+=1
    while cnt>n:
        count[word[l]]-=1
        if count[word[l]]==0:
            cnt-=1
        l+=1
    answer=max(answer,r-l+1)
    

print(answer)
    
