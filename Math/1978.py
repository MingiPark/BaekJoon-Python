if __name__=="__main__":
    numberCount = int(input())
    input = list(map(int, input().split()))

    def primeNum(a):
        if a < 2:
            return False
        i = 2
        while i*i <= a:
            if a % i == 0:
                return False
            i += 1
        return True

    count = 0
    for i in range(numberCount):
        test = primeNum(input[i])
        if test:
            count += 1
    print(count)
