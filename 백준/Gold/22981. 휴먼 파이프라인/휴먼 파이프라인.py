n,k=map(int,input().split())
number=sorted(list(map(int,input().split())))
leftN=n
rightN=0
answer= int(k/(n*number[0]))
if k%(n*number[0]): answer+=1
while True:
    leftN-=1
    if not leftN: break
    rightN+=1
    div= leftN*number[0]+rightN*number.pop()
    temp = int(k/div)
    if k%div: temp+=1
    answer=min(temp,answer)
print(answer)
