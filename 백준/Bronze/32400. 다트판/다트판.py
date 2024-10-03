target=list(map(int,input().split()))
for i in range(20):
    if target[i]==20:
        alice=target[i-1]+target[i]+target[(i+1)%20]

if alice>31.5:print('Alice')
elif alice==31.5:print('Tie')
else:print('Bob')
