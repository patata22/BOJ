def solution(numbers):
    answer = []
    
    def travel(depth, now, binaryNum):
        if depth==0: return 1
        left = now- 2**(depth-1)
        right = now+ 2**(depth-1)
        if binaryNum[now]=='0':
            if binaryNum[left]=='1' or binaryNum[right]=='1':
                return 0
        return travel(depth-1,left,binaryNum)&travel(depth-1,right,binaryNum)
    
    for num in numbers:
        depth,l=0,len(bin(num)[2:])
        while 2**depth-1<l:
            depth+=1
        
        binaryNum="0"*((2**depth-1)-l)+ bin(num)[2:]
    
        answer.append(travel(depth-1, 2**(depth-1)-1, binaryNum))
    
    
    return answer