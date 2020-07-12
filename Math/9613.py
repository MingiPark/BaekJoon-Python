if __name__ == "__main__":

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    caseNum = int(input())


    for i in range(caseNum):
        k = list(map(int, input().split()))
        n = k[0]
        m = k[1:]
        result = 0
        for j in range(0, n-1):
            for k in range(j+1, n):
                result += gcd(m[j], m[k])
        print(result)




