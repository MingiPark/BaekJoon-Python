import sys

if __name__ == "__main__":
    n, m = map(int, input().split())
    result = [0] * m
    check = [False] * (n+1)

    def nAndm2(index, start, n, m):
        if index == m:
            sys.stdout.write(' '.join(map(str, result)) + "\n")
            return
        for i in range(start, n+1):
            if check[i]:
                continue
            check[i] = True
            result[index] = i
            nAndm2(index+1, i+1, n, m)
            check[i] = False

    nAndm2(0,1,n,m)