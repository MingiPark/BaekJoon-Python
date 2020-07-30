from collections import deque
from functools import reduce

if __name__ == "__main__":
    m, n = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    dist = [[-1]*m for _ in range(n)]

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    q = deque()

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                dist[i][j] = 0
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == 0 and dist[nx][ny] == -1:
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1

    ans = max([max(row) for row in dist])

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0 and dist[i][j] == -1:
                ans = -1
    print(ans)

'''
    def bfs(x, y):
        q = deque()
        q.append((x, y))
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    if matrix[nx][ny] == 0 and not check[nx][ny]:
                        q.append((nx, ny))
                        dist[nx][ny] = dist[x][y] + 1
                        check[nx][ny] = True

    one = [[1]*m for _ in range(n)]



    for j in range(n):
        for k in range(m):
            if matrix[j][k] == 1 and not check[j][k]:
                bfs(j, k)

    ans = reduce(lambda p, q: p + q, dist)
    matrix2 = reduce(lambda w, i: w+i, matrix)
    if 0 not in matrix2:
        print("0")
    elif False in check:
        print("-1")
    else:
        print(max(ans))
'''