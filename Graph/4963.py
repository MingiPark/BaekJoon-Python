import sys
# 재귀 깊이 설정
sys.setrecursionlimit(10000)

if __name__ == "__main__":

    dx = [0,0,-1,1,-1,1,-1,1]
    dy = [1,-1,-1,1,1,-1,0,0]

    def dfs(x, y, cnt):
        group[x][y] = cnt
        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < h and 0 <= ny < w:
                if group[nx][ny] == 0 and mapMatrix[nx][ny] == 1:
                    dfs(nx, ny, cnt)

    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break

        mapMatrix = [list(map(int, input().split())) for _ in range(h)]
        group = [[0]*w for _ in range(h)]
        cnt = 0

        for i in range(h):
            for j in range(w):
                if group[i][j] == 0 and mapMatrix[i][j] == 1:
                    cnt += 1
                    dfs(i, j, cnt)

        print(cnt)





