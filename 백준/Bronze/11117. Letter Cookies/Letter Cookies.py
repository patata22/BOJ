import sys
input=sys.stdin.readline

for _ in range(int(input())):
    cookie=list(input().rstrip())
    count={}
    for x in cookie:
        if x not in count:count[x]=1
        else: count[x]+=1
    for __ in range(int(input())):
        answer='YES'
        word=list(input().rstrip())
        for x in word:
            if x not in count or word.count(x)>count[x]:        
                answer='NO'
        print(answer)       