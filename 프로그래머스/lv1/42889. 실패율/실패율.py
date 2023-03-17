def solution(N, stages):
    reach=[0]*(N+2)
    for s in stages:
        reach[s]+=1
    for i in range(N,-1,-1):
        reach[i]+=reach[i+1]

    temp=[]
    for i in range(1,N+1):
        temp.append((i,reach[i]-reach[i+1],reach[i]))
    temp.sort(key=lambda x: (ratio(x[1],x[2]),i), reverse=True)
    answer=[temp[i][0] for i in range(len(temp))]
    return answer

def ratio(a,b):
    if b==0: return 0
    else: return a/b
