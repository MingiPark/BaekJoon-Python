import sys

if __name__=="__main__":
    n, m = map(int, input().split())

    lists = [False]*(n+1)
    result = [0] * m

    def perm(index, n, m):
        if index == m:
            sys.stdout.write(' '.join(map(str, result)) + "\n")
            return
        for j in range(1, n+1):
            if lists[j]:
                continue
            lists[j] = True
            result[index] = j
            perm(index+1, n, m)
            lists[j] = False

    perm(0, n, m)
