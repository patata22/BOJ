def solution(msg):
    l=len(msg)
    dictionary={}
    for i in range(65,91):
        dictionary[chr(i)]=i-64
    answer = []
    count=27
    i=0
    while i<l:
        start=i
        end=start
        while msg[start:end+1] in dictionary and end<l:
            end+=1
        answer.append(dictionary[msg[start:end]])
        dictionary[msg[start:end+1]]=count
        count+=1
        i=end
    return answer