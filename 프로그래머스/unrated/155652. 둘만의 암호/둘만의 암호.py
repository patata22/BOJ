def solution(s, skip, index):
    atod={}
    dtoa={}
    count=0
    for i in range(97, 123):
        if chr(i) in skip: continue
        atod[chr(i)]=count
        dtoa[count]=chr(i)
        count+=1
    answer = ''
    print(atod)
    print(dtoa)
    for x in s:
        answer+= dtoa[(atod[x]+index)%count]
    return answer