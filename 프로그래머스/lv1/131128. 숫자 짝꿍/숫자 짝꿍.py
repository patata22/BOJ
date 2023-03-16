def solution(X, Y):
    record={}
    for i in range(0,10):
        record[chr(i+48)]=i
    count1=[0]*10
    count2=[0]*10
    for x in X:
        count1[record[x]]+=1
    for x in Y:
        count2[record[x]]+=1
    answer = []
    for i in range(9,-1,-1):
        if(min(count1[i],count2[i])):
            answer.append(str(i)*min(count1[i],count2[i]))
    
    if not answer: return "-1"
    if answer and answer[0][0]=='0':return "0"
    else: return ''.join(answer)
    
    
    