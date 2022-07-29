from collections import deque


n,w,L=map(int,input().split())
bridge=deque([0]*w)

truck=deque(map(int,input().split()))
t=1
bridge[-1]=truck.popleft()
while truck or sum(bridge):
    t+=1
    bridge.popleft()
    if truck and truck[0]+sum(bridge)<=L:
        bridge.append(truck.popleft())
    else: bridge.append(0)

print(t)
