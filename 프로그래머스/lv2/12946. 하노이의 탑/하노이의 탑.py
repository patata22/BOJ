def solution(n):
    answer = []
    
    def hanoi(start,end,depth):
        if depth==1:
            answer.append((start,end))
            return
        hanoi(start,6-start-end,depth-1)
        hanoi(start,end,1)
        hanoi(6-start-end, end, depth-1)
    hanoi(1,3,n)
    return answer