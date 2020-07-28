from collections import deque

if __name__ == "__main__":
    n, m = map(int, input().split())
    matrix = [list(map(int, input())) for _ in range(n)]

    dist = [[0]*m for _ in range(n)]
    check = [[False]*m for _ in range(n)]

    check[0][0] = True
    dist[0][0] = 1

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == 1 and not check[nx][ny]:
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1
                    check[nx][ny] = True

    print(dist[n-1][m-1])
