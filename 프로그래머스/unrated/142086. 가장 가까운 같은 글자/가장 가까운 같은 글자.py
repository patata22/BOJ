def solution(s):
    record={}
    answer = []
    for i in range(len(s)):
        if s[i] not in record:
            answer.append(-1)
        else:
            answer.append(i-record[s[i]])
        record[s[i]]=i
    return answer