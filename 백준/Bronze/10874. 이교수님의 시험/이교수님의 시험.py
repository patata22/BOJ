n=int(input())
for _ in range(1,n+1):
    answer=0
    temp = list(map(int,input().split()))
    for i in range(1,len(temp)+1):
        if temp[i-1]== (i-1)%5+1: answer+=1
    if answer==len(temp):print(_)
        
