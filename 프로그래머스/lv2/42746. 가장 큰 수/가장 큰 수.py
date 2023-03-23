def solution(numbers):
    def change(x):
        temp=x
        while len(temp)<4: temp+=x
        return temp[:4]
    
    answer = ''.join(sorted(map(str, numbers), key=lambda x: change(x), reverse=True))
    if answer[0]=='0':return '0'
    return answer