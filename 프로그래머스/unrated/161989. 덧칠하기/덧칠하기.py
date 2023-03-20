def solution(n, m, section):
    color = [1]*(n+1)
    for part in section:
        color[part]=0
    
    answer = 1
    for i in range(section[-1], section[-1]-m, -1):
        color[i]=1
    for i in range(n):
        if not color[i]:
            answer+=1
            for j in range(i,i+m):
                color[j]=1
    return answer