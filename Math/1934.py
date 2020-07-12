if __name__ == "__main__":
    caseCount = int(input())

    def gcd(a,b):
        if b == 0:
            return a
        else:
            return gcd(b,a%b)

    def lsm(a,b):
        return int(a*b / gcd(a,b))

    resultList = [0]*1000
    count = 0

    for i in range(caseCount):
        a,b = map(int, input().split())
        result = lsm(a,b)
        resultList[count] = result
        count+=1

    for i in range(caseCount):
        print(resultList[i])

