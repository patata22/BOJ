def solution(n):
    if n==1: return 2
    temp=list(bin(n)[2:])
    l=len(temp)
    for i in range(l-1,0,-1):
        if temp[i]=='0':
            for j in range(i+1, l):
                if temp[j]=='1':
                    temp2=temp[j+1:]
                    temp2.sort()
                    temp=temp[:j+1]+temp2
                    temp[i],temp[j]=temp[j],temp[i]
                    return int(''.join(temp),2)
    
    temp= ['1','0']+ sorted(temp[1:])
    return int(''.join(temp),2)