num={}
for i in range(97,123):
    num[chr(i)]=i-97
    num[i-97]=chr(i)

while True:
    temp=input().split()
    if temp[0]=='#':break
    answer=[]
    a,b,c=temp
    for i in range(len(a)):
        answer.append(num[(num[c[i]]+num[b[i]]-num[a[i]])%26])
    print(*temp,''.join(answer))

