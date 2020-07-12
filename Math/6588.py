if __name__=="__main__":
    MAX = 1000000
    testCase = [0]*(MAX+1)
    testCase[0] = testCase[1] = True
    prime = []

    for i in range(2, MAX+1):
        if not testCase[i]:
           prime.append(i)
           j = i+i
           while j <= MAX:
            testCase[j] = True
            j += i
    prime = prime[1:]

    while True:
        k = int(input())
        if k == 0:
            break
        for i in prime:
            if not testCase[k - i]:
                print("{0} = {1} + {2}".format(k, i, k-i))
                break




