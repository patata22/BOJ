temp=list(map(int,list(input())))
for _ in range(int(input())):
    guess=list(map(int,list(input())))
    ball=0
    for x in guess:
        if x in temp: ball+=1
    strike=0
    for i in range(4):
        if temp[i]==guess[i]: strike+=1
    print(ball,strike)