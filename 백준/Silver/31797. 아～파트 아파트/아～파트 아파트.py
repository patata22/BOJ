n,m=map(int,input().split())

hand=[]
for i in range(1,m+1):
    a,b=map(int,input().split())
    hand.append([a,i])
    hand.append([b,i])
hand.sort()
finish=False
for i in range(2*m):
    hand[i][0]=i+1

while not finish:
    for i in range(2*m):
        if hand[i][0]==n:
            print(hand[i][1])
            finish=True
            break
        else:
            hand[i][0]+=2*m
            
