from collections import Counter

def solution(topping):
    count= Counter(topping)
    left=set(topping)
    right=set()
    answer = 0
    l,r=len(left), 0
    while topping:
        now=topping.pop()
        count[now]-=1
        if not count[now]: 
            l-=1
        if now not in right:
            r+=1
            right.add(now)
        if l==r: answer+=1
    return answer