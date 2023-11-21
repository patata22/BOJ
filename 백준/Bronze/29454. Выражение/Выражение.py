n=int(input())
card=tuple(map(int,input().split()))
total=sum(card)
for i in range(n):
    if total==2*card[i]:
        print(i+1)
        break
