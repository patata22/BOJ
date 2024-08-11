while True:
    m=int(input())
    if not m: break
    word=list(input())
    n=len(word)
    count={}
    for x in word:
        count[x]=0
    l=-1
    r=0
    answer=0
    cnt=0
    while l+1<n:
        l+=1
        now=word[l]
        if count[now]==0: cnt+=1
        count[now]+=1
        while cnt>m:
            count[word[r]]-=1
            if count[word[r]]==0:
                cnt-=1
            r+=1
        answer=max(answer,l-r+1)
    print(answer)
