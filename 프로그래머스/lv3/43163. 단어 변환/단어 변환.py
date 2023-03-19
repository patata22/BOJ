from collections import deque

def solution(begin, target, words):
    n=len(words)
    
    q=deque()
    visited=set()
    graph={}
    for x in words:
        graph[x]=[]
        if distance(x, begin)==1:
            q.append(x)
            visited.add(x)
    for i in range(n):
        a=words[i]
        for j in range(i+1, n):
            b=words[j]
            if distance(a,b)==1:
                graph[a].append(b)
                graph[b].append(a)
    
    t=1
    while q:
        for _ in range(len(q)):
            now = q.popleft()
            if now==target: return t
            for to in graph[now]:
                if to not in visited: 
                    visited.add(to)
                    q.append(to)
        t+=1
    
    return 0


def distance(a,b):
    count=0
    for i in range(len(a)):
        if a[i]!=b[i]:count+=1
    return count