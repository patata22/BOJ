trans={0:'ZERO', 1:'ONE', 2:'TWO', 3:'THREE', 4:'FOUR', 5:'FIVE', 6:'SIX', 7:'SEVEN', 8:'EIGHT', 9:'NINE'}
cnt={}
for i in range(10):
    temp=[0]*26
    for x in trans[i]:
        temp[ord(x)-65]+=1
    cnt[i]=temp
def sol(start, now):
    global flag,answer
    if sum(count)==0:
        flag=True
        answer=now
    if flag:return
    for i in range(start,10):
        check=True
        temp=cnt[i]
        for j in range(26):
            if count[j]-temp[j]<0:
                check=False
                break
        if check:
            for j in range(26): count[j]-=temp[j]
            sol(i, now+str(i))
            for j in range(26): count[j]+=temp[j]
                
for _ in range(int(input())):
    temp=input()
    count=[0]*26
    answer=""
    flag=False
    for x in temp:count[ord(x)-65]+=1
    sol(0,"")
    print(f'Case #{_+1}: {answer}')
