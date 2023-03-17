def solution(sizes):
    
    x,y=0,0
    for a,b in sizes:
        if b>=a: a,b=b,a
        x=max(x,a)
        y=max(y,b)
    
    return (x*y)