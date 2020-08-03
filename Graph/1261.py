from collections import deque

if __name__ == "__main__":
    m, n = map(int, input().split())
    matrix = [list(map(int, input())) for _ in range(n)]
    check = [[False]*m for _ in range(n)]
    dist = [[0]*m for _ in range(n)]

    q = deque()
    q.append((0, 0))

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == 0 and not check[nx][ny]:
                    check[nx][ny] = True
                    dist[nx][ny] = dist[x][y]
                    q.appendleft((nx, ny))
                if matrix[nx][ny] == 1 and not check[nx][ny]:
                    check[nx][ny] = True
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

    print(dist[n-1][m-1])



