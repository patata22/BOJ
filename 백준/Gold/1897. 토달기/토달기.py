from collections import deque

def sol():
    q=deque()
    q.append(start)
    answer=start
    while q:
        now=q.popleft()
        for i in range(len(now)):
            head = now[0:i]
            tail = now[i:len(now)]
            for j in range(97,123):
                temp = head+chr(j)+tail
                if temp in dictionary and temp not in visited:
                    q.append(temp)
                    visited.add(temp)
                    answer=(temp)
        for j in range(97,123):
            if now+chr(j) in dictionary and now+chr(j) not in visited:
                visited.add(now+chr(j))
                answer=now+chr(j)
                q.append(now+chr(j))
        
    return answer

n,start=input().split()
dictionary = set()
visited=set()
for _ in range(int(n)):
    dictionary.add(input())

print(sol())
