if __name__=="__main__":
    n = int(input())
    check = [list(map(int, input().split())) for _ in range(n)]

    number = list(range(n))

    def usePermutation(a):

        j = len(a) - 1
        while j > 0 and a[j-1] >= a[j]:
            j -= 1
        if j <= 0:
            return False

        k = len(a) - 1
        while a[k] <= a[j-1]:
            k -= 1

        a[k], a[j-1] = a[j-1], a[k]

        l = len(a)-1
        while j < l:
            a[j], a[l] = a[l], a[j]
            j += 1
            l -= 1

        return True

    minResult = 2147483647

    while True:
        result = 0
        ok = True
        for i in range(n-1):
            if check[number[i]][number[i+1]] == 0:
                ok = False
                break
            else:
                result += check[number[i]][number[i + 1]]
        if ok and check[number[-1]][number[0]] != 0:
                result += check[number[-1]][number[0]]
                minResult = min(result, minResult)
        if not usePermutation(number):
            break

    print(minResult)
