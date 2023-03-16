def solution(wallpaper):
    minX,minY=float('inf'),float('inf')
    maxX,maxY=-float('inf'), -float('inf')
    n=len(wallpaper)
    m=len(wallpaper[0])
    for x in range(n):
        for y in range(m):
            if wallpaper[x][y]=='#':
                minX=min(minX, x)
                minY=min(minY, y)
                maxX=max(maxX, x+1)
                maxY=max(maxY, y+1)
    return (minX,minY,maxX,maxY)