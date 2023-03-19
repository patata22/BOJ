from collections import deque

def solution(n, computers):
    answer = 0
    visited=[0]*n
    for i in range(n):
        if not visited[i]:
            answer+=1
            q=deque()
            q.append(i)
            visited[i]=1
            while q:
                now=q.popleft()
                for j in range(n):
                    if computers[now][j] and not visited[j]:
                        visited[j]=1
                        q.append(j)
    return answer

