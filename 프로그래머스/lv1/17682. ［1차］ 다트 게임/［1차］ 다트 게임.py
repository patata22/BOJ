def solution(dartResult):
    answer = 0
    lastScore=0
    currentScore=0
    bonus={'S':1, 'D':2, 'T':3}
    temp=""
    for x in dartResult: 
        if x.isdigit():
            temp+=x
        elif x in bonus:
            answer+=currentScore
            lastScore, currentScore = currentScore, int(temp)
            temp=""
            currentScore**=bonus[x]
        elif x == '*':
            answer+=lastScore
            currentScore*=2
        elif x == '#':
            currentScore*=-1
        print(x,currentScore)
    answer+=currentScore
    return answer