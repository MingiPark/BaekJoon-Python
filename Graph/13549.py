from collections import deque

if __name__ == "__main__":
    n, m = map(int, input().split())
    MAX = 200000
    check = [False for _ in range(MAX + 1)]
    dist = [0 for _ in range(MAX + 1)]

    check[n] = True
    dist[n] = 0

    q = deque()
    q.append(n)

    while q:
        now = q.popleft()
        if 0 <= now*2 < MAX and not check[now*2]:
            check[now*2] = True
            dist[now*2] = dist[now]
            q.appendleft(now*2)
        if 0 <= now+1 < MAX and not check[now+1]:
            check[now+1] = True
            dist[now+1] = dist[now] + 1
            q.append(now+1)
        if 0 <= now-1 < MAX and not check[now-1]:
            check[now-1] = True
            dist[now-1] = dist[now] + 1
            q.append(now-1)

    print(dist[m])
