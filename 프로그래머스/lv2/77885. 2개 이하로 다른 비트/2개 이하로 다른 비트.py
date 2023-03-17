def solution(numbers):
    return [change(n) for n in numbers]

def change(n):
    if n==0: return 1
    temp=list(bin(n)[2:])
    for i in range(len(temp)-1,0,-1):
        if temp[i]=='0':
            temp[i]='1'
            for i in range(i+1,len(temp)):
                if temp[i]=='1':temp[i]='0'
                break
            return int(''.join(temp),2)
    temp[0]='0'
    return int('1'+''.join(temp),2)