n,m=map(int,input().split())
box=list(map(int,input().split()))
book = list(map(int,input().split()))
bidx=0
answer=0
for x in book:
    while box[bidx]<x:
        answer+=box[bidx]
        bidx+=1
    box[bidx]-=x
answer+=sum(box[bidx:])
print(answer)
