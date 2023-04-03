def solution(k, room_number):
    answer = []
    used={}
    for number in room_number:
        temp=set()
        temp.add(number)
        while number in used:
            nxt=number+used[number]
            used[number]+=1
            number=nxt
            temp.add(number)
        answer.append(number)
        for n in temp:
            used[n]=number-n+1
        used[number]=1
    
    return answer