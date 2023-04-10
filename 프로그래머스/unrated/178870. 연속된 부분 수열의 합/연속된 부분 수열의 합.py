def solution(sequence, k):
    n=len(sequence)
    answer = []
    gap=float('inf')
    l,r=0,0
    total=sequence[0]
    while r<n:
        if total==k:
            if r-l<gap:
                gap=r-l
                answer=[l,r]
            r+=1
            if r==n: break
            total+=sequence[r]
        elif total>k:
            total-=sequence[l]
            l+=1
        elif total<k:
            r+=1
            if r==n: break
            total+=sequence[r]
            
    return answer