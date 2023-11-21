card={}
lst=[]
n=int(input())
for i in range(n):
    number=list(map(int,input().split()))
    for x in number[1:]:
        lst.append(x)
        card[x]=chr(i+65)
lst.sort()
for x in lst:
    print(card[x],end='')
    
