def solution(weights):
    answer=0
    count={}
    for weight in weights:
        if weight not in count: count[weight]=1
        else: count[weight]+=1
    
    for x in count:
        n=count[x]
        answer+=(n*n-n)//2
        if 2*x in count:
            answer+=n*count[2*x]
        if 1.5*x in count:
            
            answer+=n*count[1.5*x]
        if 3*x/4 in count:
            
            answer+=n*count[3*x/4]
            
    return answer
    