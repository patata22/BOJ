from collections import deque

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)


def sol():
    q = deque()
    for x, y in fire: q.append((x, y, 1))
    q.append((sx, sy, 0))
    visited[sx][sy] = 1
    t = 0
    while q:
        for __ in range(len(q)):
            x, y, is_fire = q.popleft()
            if not (0 <= x < n and 0 <= y < m): return t
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if is_fire:
                    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == '.' and not visited[nx][ny]:
                        visited[nx][ny] = 1
                        q.append((nx, ny, is_fire))
                else:
                    if not (0 <= nx < n and 0 <= ny < m):
                        q.append((nx, ny, is_fire))
                    else:
                        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == '.' and not visited[nx][ny]:
                            visited[nx][ny] = 1
                            q.append((nx, ny, is_fire))
        t+=1
    return "IMPOSSIBLE"


for _ in range(int(input())):
    m, n = map(int, input().split())
    board = [list(input()) for i in range(n)]
    visited = [[0] * m for i in range(n)]
    fire = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == '*':
                visited[i][j] = 1
                fire.append((i, j))
            elif board[i][j] == '@':
                board[i][j] = '.'
                sx, sy = i, j

    print(sol())
