def solution(survey, choices):
    n=len(survey)
    record={}
    type="RTCFJMAN"
    for x in type: 
        record[x]=0
    
    for i in range(n):
        a,b=survey[i][0], survey[i][1]
        if 1<=choices[i]<=3:
            record[a]+=4-choices[i]
        elif 5<=choices[i]<=7:
            record[b]+= choices[i]-4
        
    answer = ''
    
    if record["R"]>=record["T"]:answer+="R"
    else: answer+="T"
    
    if record["C"]>=record["F"]:answer+="C"
    else: answer+="F"
    
    if record["J"]>=record["M"]:answer+="J"
    else:answer+="M"
    
    if record["A"]>=record["N"]:answer+="A"
    else:answer+="N"

    return answer