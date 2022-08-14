score=sorted([list(map(int,input().split())) for i in range(int(input()))], key=lambda x: -x[2])
count={}
for x in score:
    count[x[0]]=0

finish=0
for country,number, s in score:
    if count[country]>1:continue
    else:
        count[country]+=1
        print(country,number)
        finish+=1
        if finish==3: break
        
