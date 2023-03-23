def solution(arr1, arr2):
    # (a*b) * (b*c)  = (a*c)
    a=len(arr1)
    b=len(arr1[0])
    c=len(arr2[0])
    answer = [[0]*c for i in range(a)]
    
    for i in range(a):
        for h in range(c):
            sub=0
            for j in range(b):
                sub+=arr1[i][j]*arr2[j][h]
            answer[i][h]=sub  
    
    
    
    
    
    
    
    return answer