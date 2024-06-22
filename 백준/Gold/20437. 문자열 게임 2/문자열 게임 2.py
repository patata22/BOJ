for tt in range(int(input())):
    word=list(map(lambda x: ord(x)-97, input()))
    k=int(input())
    n=len(word)
    count=[[] for i in range(26)]
    for i in range(n):
        count[word[i]].append(i)
        
    answer1=float('inf')
    answer2=0
    for cnt in count:
        for i in range(len(cnt)-k+1):
            answer1=min(answer1, cnt[i+k-1]-cnt[i])
            answer2=max(answer2, cnt[i+k-1]-cnt[i])
    if answer1==float('inf'):print(-1)
    else: print(answer1+1,answer2+1)
