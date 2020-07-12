if __name__ == "__main__":
    e, s, m = map(int, input().split())
    E, S, M = 15, 28, 19
    result = 0

    e -= 1
    s -= 1
    m -= 1

    for i in range(0,7980):
        if i % E == e and i % S == s and i % M == m:
            print(i+1)

