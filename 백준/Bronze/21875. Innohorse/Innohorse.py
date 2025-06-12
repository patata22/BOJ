def parse(pos):
    col = ord(pos[0]) - ord('a')
    row = int(pos[1]) - 1
    return (col, row)

def sol(pos1, pos2):
    x1, y1 = parse(pos1)
    x2, y2 = parse(pos2)
    dx = x2 - x1
    dy = y2 - y1
    
    for x in range(8):
        for y in range(x, 8):
            candidates = [
                (x, y), (y, x), (-x, y), (-y, x),
                (x, -y), (y, -x), (-x, -y), (-y, -x)
            ]
            if (dx, dy) in candidates:
                return x, y

print(*sol(input(),input()))
