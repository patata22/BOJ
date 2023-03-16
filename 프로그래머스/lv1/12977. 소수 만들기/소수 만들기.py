def solution(nums):
    answer=0
    n=len(nums)
    
    seive()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if isPrime[nums[i]+nums[j]+nums[k]]: answer+=1
    return answer

def seive():
    for i in range(2,3000):
        if isPrime[i]:
            for i in range(i+i,3000,i):
                isPrime[i]=0
                
isPrime=[1]*3000
isPrime[0]=0
isPrime[1]=1
