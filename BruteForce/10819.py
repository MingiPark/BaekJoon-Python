if __name__=="__main__":
    n = int(input())
    check = list(map(int, input().split()))
    check.sort()

    def nextpermutation(a):
        i = len(a)-1
        while i > 0 and a[i-1] >= a[i]:
            i -= 1
        if i <= 0:
            return False

        j = len(a)-1
        while a[j] <= a[i-1]:
            j -= 1

        a[j], a[i-1] = a[i-1], a[j]

        k = len(a)-1
        while i < k:
            a[i], a[k] = a[k], a[i]
            i += 1
            k -= 1

        return True

    def cal(a):
        result = 0
        for i in range(n-1):
            result += abs(a[i+1] - a[i])
        return result

    answer = 0
    while True:
        maxValue = cal(check)
        answer = max(maxValue, answer)
        if not nextpermutation(check):
            break

    print(answer)