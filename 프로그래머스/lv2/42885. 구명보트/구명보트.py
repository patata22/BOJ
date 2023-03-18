def solution(people, limit):
    people.sort()
    answer = 0
    
    n=len(people)
    crt = 0
    for i in range(n):
        if people[i]>limit//2:
            crt=i
            break
            
    over= people[crt:]
    under= people[:crt][::-1]
    while over and under:
        if over[-1]+under[-1]<=limit:
            under.pop()
        over.pop()
        answer+=1
    answer+= (len(under)+1)//2
    answer+= (len(over))
    
    return answer