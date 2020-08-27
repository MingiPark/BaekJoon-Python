if __name__ == "__main__":
    n = int(input())
    value = [[0]*10 for _ in range(100+1)]
    mod = 1000000000

    for i in range(1, 10):
        value[1][i] = 1

    for j in range(2, n+1):
        for k in range(10):
            if k-1 >= 0:
                value[j][k] = value[j][k] + value[j-1][k-1]
            if k+1 <= 9:
                value[j][k] = value[j][k] + value[j-1][k+1]

    ans = sum(value[n]) % mod
    print(ans)



