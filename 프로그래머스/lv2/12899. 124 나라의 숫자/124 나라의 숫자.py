def solution(n):
    answer=""
    while n:
        if not n%3: 
            answer+='4'
            n=n//3-1
        else:
            answer+=str(n%3)
            n//=3
    return answer[::-1]