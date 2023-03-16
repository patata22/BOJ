def solution(s):
    answer = ''
    temp=""
    for x in s:
        if x==' ':
            if temp: answer+=change(temp)
            temp=""
            answer+=' '
        else: temp+=x
    if temp: answer+=change(temp)
    return answer

def change(word):
    result=""
    for i in range(len(word)):
        if i%2: result+=word[i].lower()
        else: result+=word[i].upper()
    return result