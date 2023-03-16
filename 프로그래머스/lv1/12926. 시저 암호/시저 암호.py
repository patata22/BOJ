def solution(s, n):
    
    answer = ''
    for x in s: answer+=change(x,n)
    return answer

def change(x,n):
    if x==' ': return ' '
    elif x.isupper():
        return chr((ord(x)-65+n)%26+65)
    else: return chr((ord(x)-97+n)%26+97)