import sys

if __name__ == "__main__":
    n, m = map(int, input().split())

    tf = [[False]*n for _ in range(n)]
    edges = []
    adjList = [[] for _ in range(n)]

    for i in range(m):
        start, finish = map(int, input().split())

        edges.append((start, finish))
        edges.append((finish, start))

        tf[start][finish] = tf[finish][start] = True

        adjList[start].append(finish)
        adjList[finish].append(start)

    m *= 2

    for j in range(m):
        for k in range(m):
            A, B = edges[j]
            C, D = edges[k]
            #각각 모두 다른 정점인지 확인
            if A==B or A==C or A==D or B==C or B==D or C==D:
                continue
            #B와 C가 연결 되어 있는 지 확인
            if not tf[B][C]:
                continue
            #D와 연결되어 있는 정점이 기존 A,B,C,D와 다른 지 확인
            for E in adjList[D]:
                if A==E or B==E or C==E or D==E:
                    continue
                print(1)
                sys.exit(0)
    print(0)