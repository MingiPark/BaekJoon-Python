import sys

if __name__ == "__main__":
    n, m = map(int, input().split())

    numList = list(map(int, input().split()))
    numList.sort()

    check = [False]*(n+1)
    result = [0]*m

    def nAndm5(index, n, m):
        if index == m:
            sys.stdout.write(' '.join(map(str, result)) + "\n")
            return
        for i in range(n):
            if check[i]:
                continue
            check[i] = True
            result[index] = numList[i]
            nAndm5(index+1, n, m)
            check[i] = False

    nAndm5(0, n, m)