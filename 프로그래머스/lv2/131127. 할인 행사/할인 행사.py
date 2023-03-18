def solution(want, number, discount):
    count={}
    need={}
    for i in range(len(want)):
        x=want[i]
        count[x]=0
        need[x]=number[i]
    answer=0
    
    n=len(discount)
    for i in range(10):
        x=discount[i]
        if x in count: count[x]+=1
    answer+=check(count,need)
    for i in range(10,n):
        if discount[i-10] in count: count[discount[i-10]]-=1
        if discount[i] in count: count[discount[i]]+=1
        answer+=check(count,need)
    return answer

def check(count, need):
    for x in count:
        if count[x]<need[x]: return 0
    return 1