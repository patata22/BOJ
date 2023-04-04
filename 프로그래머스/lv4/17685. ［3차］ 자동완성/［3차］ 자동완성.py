def solution(words):
    answer = 0
    
    unused=2
    MAX=1000005
    nxt=[[-1]*26 for i in range(MAX)]
    check=[0]*MAX
    
    def insert(s):
        nonlocal unused
        now=1
        for x in s:
            char=ord(x)-97
            if nxt[now][char]==-1:
                
                nxt[now][char]=unused
                unused+=1
            check[now]+=1
            now=nxt[now][char]
        check[now]+=1
    
    def find(s):
        flag=True
        t=0
        now=1
        for x in s:
            if flag:t+=1
            char=ord(x)-97
            now=nxt[now][char]
            if check[now]==1:
                flag=False
            #print(s,x,t,flag,check[now])
        return t
    
    for word in words: insert(word)
    for word in words:
        answer+=find(word)
    
    return answer
