if __name__ == "__main__":
    n = int(input())
    v = [[0]*10 for _ in range(1000+1)]

    for i in range(10):
        v[1][i] = 1

    for j in range(2, n+1):
        for k in range(10):
            for l in range(k+1):
                v[j][k] += v[j-1][l]

    ans = sum(v[n])
    print(ans % 10007)

