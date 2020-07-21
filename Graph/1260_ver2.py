from collections import deque

if __name__=="__main__":
    n, m, v = map(int, input().split())
    edges = [[] for _ in range(n+1)]
    check = [False] * (n+1)

    for _ in range(m):
        s, f = map(int, input().split())
        edges[s].append(f)
        edges[f].append(s)

    for i in range(n):
        edges[i].sort()


    # 인접 리스트 활용

    def dfs(x):
        global check
        check[x] = True
        print(x, end=' ')
        for y in edges[x]:
            if not check[y]:
                dfs(y)


    def bfs(v):
        check = [False] * (n + 1)
        q = deque()
        q.append(v)
        check[v] = True
        while q:
            x = q.popleft()
            print(x, end=' ')
            for y in edges[x]:
                if not check[y]:
                    check[y] = True
                    q.append(y)

    dfs(v)
    print()
    bfs(v)
    print()

