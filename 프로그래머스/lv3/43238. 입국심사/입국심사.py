def solution(n, times):
    answer = 0
    l=1
    r=min(times)*n +1
    while l+1<r:
        mid=(l+r)//2
        temp=0
        for t in times: temp+=mid//t
        if temp>=n: r=mid
        else: l=mid
        
    return r