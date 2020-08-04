from collections import deque

if __name__ == "__main__":
    m, n = map(int, input().split())
    matrix = [list(map(str, input())) for _ in range(m)]
    dist1 = [[0]*n for _ in range(m)]
    dist2 = [[0]*n for _ in range(m)]

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    q1 = deque()
    q2 = deque()
    ans1, ans2 = 0, 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '*':
                q1.append((i, j))
            elif matrix[i][j] == 'S':
                q2.append((i, j))
                k1, k2 = i, j
            elif matrix[i][j] == 'D':
                ans1, ans2 = i, j

    while q1:
        x, y = q1.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if dist1[nx][ny] == 0 and matrix[nx][ny] == '.':
                    dist1[nx][ny] = dist1[x][y] + 1
                    q1.append((nx, ny))

    dist1[ans1][ans2] = max(map(max, dist1)) + 100
    k = dist1[ans1][ans2]

    for i in range(m):
        for j in range(n):
            if dist1[i][j] == 0 and matrix[i][j] == '.':
                dist1[i][j] = k

    while q2:
        x, y = q2.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < m and 0 <= ny < n:
                if dist2[nx][ny] == 0 and (matrix[nx][ny] == '.' or matrix[nx][ny] == 'D') and dist2[x][y]+1 < dist1[nx][ny]:
                    dist2[nx][ny] = dist2[x][y] + 1
                    q2.append((nx, ny))

    if dist2[ans1][ans2] == 0:
        print("KAKTUS")
    else:
        print(dist2[ans1][ans2])
