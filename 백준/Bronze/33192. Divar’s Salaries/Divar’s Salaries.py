def sol():
    x,k,h=map(int,input().split())
    answer=0
    answer+=2*h*x
    k-=h
    over=max(0,k-140)
    answer+=15*over*x//10
    answer+=min(140,k)*x
    answer=list(str(answer))
    result=[]
    cnt=0
    while answer:
        cnt+=1
        result.append(answer.pop())
        if cnt%3==0 and answer: result.append(',')
    print(''.join(result[::-1]))

for tt in range(int(input())):
    sol()
