from collections import deque, Counter
from functools import reduce

#BFS CASE
if __name__ == "__main__" :
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    n = int(input())
    mapMatrix = [list(map(int, input())) for _ in range(n)]
    group = [[0]*n for _ in range(n)]
    cnt = 0

    def bfs(x, y, cnt):
        q = deque()
        q.append((x, y))
        group[x][y] = cnt
        while q:
            x, y = q.popleft()
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if mapMatrix[nx][ny] == 1 and group[nx][ny] == 0:
                        q.append((nx, ny))
                        group[nx][ny] = cnt

    for i in range(n):
        for j in range(n):
            if mapMatrix[i][j] == 1 and group[i][j] == 0:
                cnt += 1
                # 하나의 단지를 찾아낸다.
                bfs(i, j, cnt)

    #group의 행렬을 하나의 행으로 합친다.
    ans = reduce(lambda x, y: x+y, group)
    #행렬의 값 중 0을 제거한다.
    ans = [x for x in ans if x > 0]
    #각 단지 내 집의 수를 세어 값을 계산한다.(Sorted : 오름차순 정렬)
    ans = sorted(list(Counter(ans).values()))
    print(cnt)
    print('\n'.join(map(str, ans)))
