if __name__=="__main__":
    n = int(input())
    a = [0] * n
    for i in range(1, n + 1):
        a[i-1] = i

    def allPermutation(a):

        # 뒤에서부터 감소수열 끝나는 점 바로 앞의 값 찾기
        i = len(a) - 1
        while i > 0 and a[i - 1] >= a[i]:
            i -= 1
        if i <= 0:
            return False

        # 감소수열 중 바로 앞의 값보다 큰 값 찾고 swap
        j = len(a) - 1
        while a[j] <= a[i - 1]:
            j -= 1

        a[i - 1], a[j] = a[j], a[i - 1]

        # 순열 뒤집기
        j = len(a) - 1
        while i < j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
        print(' '.join(map(str, a)))
        return True


    print(' '.join(map(str, a)))
    while True:
        if allPermutation(a):
            allPermutation(a)
        else:
            break
