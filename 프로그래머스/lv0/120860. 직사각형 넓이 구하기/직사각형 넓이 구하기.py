def solution(dots):
    minX,minY=float('inf'),float('inf')
    maxX,maxY=-float('inf'), -float('inf')
    for x,y in dots:
        minX=min(x,minX)
        maxX=max(x,maxX)
        minY=min(y,minY)
        maxY=max(y,maxY)
    return (maxX-minX)*(maxY-minY)