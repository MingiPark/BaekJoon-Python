if __name__ == "__main__":
    n = int(input())
    check = list(map(int, input().split()))

    def prePermutation(a):

        i = len(a)-1
        while i>0 and a[i-1] <= a[i]:
            i -= 1
        if i<=0:
            return False

        j = len(a)-1
        while a[j] >= a[i-1]:
            j -= 1

        a[i-1],a[j] = a[j], a[i-1]

        k = len(a)-1
        while i < k:
            a[i], a[k] = a[k], a[i]
            i += 1
            k -= 1

        return True

    if prePermutation(check):
        print(' '.join(map(str, check)))
    else:
        print(-1)