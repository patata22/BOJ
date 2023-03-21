def solution(prices):
    answer = [0]*len(prices)
    
    #0: index, 1: price
    prices=[(i,x) for i,x in enumerate(prices)]
    stack=[]
    for index,price in prices:
        while stack and stack[-1][-1]>price:
            i,x=stack.pop()
            answer[i]=index-i
        stack.append((index,price))
    while stack:
        i,x=stack.pop()
        answer[i]=len(prices)-i-1
    
    return answer