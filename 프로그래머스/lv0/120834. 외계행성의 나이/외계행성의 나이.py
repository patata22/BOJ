def solution(age):
    answer = ''
    while age:
        answer+=chr(age%10+97)
        age//=10
    return answer[::-1]