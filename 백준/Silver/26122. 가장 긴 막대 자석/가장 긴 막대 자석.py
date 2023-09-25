n=int(input())
string=input()
now=string[0]
cnt=1
number=[]
for i in range(1,n):
    if string[i]!=now:
        now=string[i]
        number.append(cnt)
        cnt=1
    else:
        cnt+=1
number.append(cnt)
answer=0
for i in range(1,len(number)):
    answer=max(answer,2*min(number[i],number[i-1]))
print(answer)
    
