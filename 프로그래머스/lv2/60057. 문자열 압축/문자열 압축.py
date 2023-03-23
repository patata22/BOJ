def solution(s):
    n=len(s)
    answer=n
    def compress(x,length):
        result=""
        count=1
        now=x[:length]
        i=0
        while i<len(x):
            i+=length
            temp = x[i:i+length]
            if temp==now:
                count+=1
            else:
                if count==1: result+=now
                else: result += str(count)+now
                count=1
                now=temp
        return len(result)
    
    for i in range(1,n//2+1):
        answer=min(compress(s,i), answer)
    
    return answer