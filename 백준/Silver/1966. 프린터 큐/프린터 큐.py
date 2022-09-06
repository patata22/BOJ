from collections import deque

for _ in range(int(input())):
    n,m=map(int,input().split())
    cnt=0
    paper=list(map(int,input().split()))
    q=deque(enumerate(paper))
    paper.sort()
    
    while q:
        num,priority=q.popleft()
        if priority==paper[-1]:
            paper.pop()
            cnt+=1
            if num==m:
                print(cnt)
                break
        else: q.append((num,priority))