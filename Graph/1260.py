from collections import deque

if __name__ == "__main__":
    n, m, v = map(int, input().split())
    edges = []
    check = [False]*(n+1)

    for _ in range(m):
        s, f = map(int, input().split())
        edges.append((s, f))
        edges.append((f, s))

    m *= 2
    edges.sort()
    cnt = [0]*(n+1)

    for s, f in edges:
        cnt[s] += 1

    for i in range(1, n+1):
        cnt[i] += cnt[i-1]

# 간선 리스트 활용
    def dfs(x):
        global check
        check[x] = True
        print(x, end=' ')
        for j in range(cnt[x-1], cnt[x]):
            y = edges[j][1]
            if not check[y]:
                dfs(y)

    def bfs(v):
        check = [False]*(n+1)
        q = deque()
        q.append(v)
        check[v] = True
        while q:
            x = q.popleft()
            print(x, end=' ')
            for k in range(cnt[x-1], cnt[x]):
                y = edges[k][1]
                if not check[y]:
                    check[y] = True
                    q.append(y)

    dfs(v)
    print()
    bfs(v)
    print()

