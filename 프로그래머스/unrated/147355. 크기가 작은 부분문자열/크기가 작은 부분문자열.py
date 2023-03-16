def solution(t, p):
    n=len(p)
    p=int(p)
    global answer
    answer = 0
    for i in range(0,len(t)-n+1):
        print(int(t[i:i+n]))
        if int(t[i:i+n])<=p:
            answer+=1
    return answer
