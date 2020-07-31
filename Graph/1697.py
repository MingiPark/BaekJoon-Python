from collections import deque

if __name__ == "__main__":
    n, k = map(int, input().split())
    MAX = 100000
    check = [False for _ in range(MAX+1)]
    check[n] = True
    dist = [0 for _ in range(MAX+1)]

    q = deque()
    q.append(n)

    while q:
        now = q.popleft()
        for nxt in [now - 1, now + 1, now * 2]:
            if 0 <= nxt <= MAX and not check[nxt]:
                check[nxt] = True
                dist[nxt] = dist[now] + 1
                q.append(nxt)

    print(dist[k])
