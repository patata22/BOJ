n,now=map(int,input().split())
voice=list(map(int,input().split()))
i=0
while True:
    if voice[i]<now:
        print(i+1)
        break
    now+=1
    i=(i+1)%n

