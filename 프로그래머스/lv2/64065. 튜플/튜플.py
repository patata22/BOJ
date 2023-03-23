def solution(s):
    
    answer = []
    record=set()
    s=s.split('},{')
    s[0]=s[0].lstrip('{')
    s[-1]=s[-1].rstrip('}')
    for i in range(len(s)):
        s[i] = list(map(int,s[i].split(',')))
    s.sort(key=lambda x: len(x))
    for numbers in s:
        for number in numbers:
            if number not in record:
                record.add(number)
                answer.append(number)
    
    
    return answer