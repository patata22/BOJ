n=int(input())
cmd=[tuple(map(lambda x: int(x)-1, input().split())) for i in range(n)]
answer=[0,0,0]
stones=([1,0,0],[0,1,0],[0,0,1])
for i in range(3):
    stone=stones[i]
    for a,b,c in cmd:
        stone[a],stone[b]=stone[b],stone[a]
        if stone[c]:answer[i]+=1
    
print(max(answer))
            