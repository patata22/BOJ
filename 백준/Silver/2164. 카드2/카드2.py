from collections import deque

card = deque([i for i in range(int(input()))])
while len(card)>1:
    card.popleft()
    card.append(card.popleft())
print(card[0]+1)
