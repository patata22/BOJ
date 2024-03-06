def sol():
    candi = list(map(lambda x: ord(x)-97,input()))
    cnt=[0]*26
    N=len(candi)
    if n>N: return 'NO'
    
    for i in range(n):
        cnt[candi[i]]+=1
    gap=0
    l=0
    r=n-1
    for i in range(26):
        gap+=abs(cnt[i]-oriCnt[i])
    
    if n==N:
        if gap==2: return 'YES'
        else: return 'NO'
    if 0<gap<=2: return 'YES'
    while r<N-1:
        r+=1
        right=candi[r]
        if cnt[right]>=oriCnt[right]:gap+=1
        else: gap-=1
        cnt[right]+=1
        left=candi[l]
        if cnt[left]>oriCnt[left]: gap-=1
        else: gap+=1
        cnt[left]-=1
        l+=1
        if gap<=2: return 'YES'
    
    return 'NO'
    
original=list(map(lambda x: ord(x)-97, input()))
n=len(original)     
oriCnt=[0]*26
for x in original: oriCnt[x]+=1
for _ in range(int(input())):
    print(sol())
