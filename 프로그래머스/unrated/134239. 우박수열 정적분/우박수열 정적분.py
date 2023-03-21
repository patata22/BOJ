def solution(k, ranges):
    answer = []
    number=[]
    while k!=1:
        number.append(k)
        if k%2: k=k*3+1
        else: k//=2
    number.append(1)
    n=len(number)
    for start, end  in ranges:
        end = n+end-1
        if end<start: answer.append(-1)
        else:
            temp=0
            for i in range(start,end):
                temp+= (number[i]+number[i+1])/2
            answer.append(temp)

    return answer