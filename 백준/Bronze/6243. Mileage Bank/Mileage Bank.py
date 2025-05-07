answer=0
while True:
    temp=input().split()
    if temp[0]=='0':
        print(answer)
        answer=0
        continue
    elif temp[0]=='#':break
    typ=temp[3]
    mile=int(temp[2])
    if typ=='F': answer+=2*mile
    elif typ=='B': answer+=round(1.5*mile+0.00001)
    elif typ=='Y': answer+=max(500,mile)

