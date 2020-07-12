import sys

if __name__ == "__main__":
    n, m = map(int, input().split())
    check = [False] * (n+1)
    result = [0] * m

    def nAndm3(index, start, n, m):
        if index == m:
            sys.stdout.write(' '.join(map(str, result)) + "\n")
            return
        for i in range(start, n+1):
            check[i] = True
            result[index] = i
            nAndm3(index+1, i, n, m)
            check[i] = False

    nAndm3(0, 1, n, m)