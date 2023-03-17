def solution(brown, yellow):
    temp= (brown//2)+2

    for i in range(3,temp):
        j=temp-i
        if (i-2)*(j-2)==yellow: return (j,i)
        
    return answer