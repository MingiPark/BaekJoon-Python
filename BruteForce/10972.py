if __name__ == "__main__":
    n = int(input())
    checkList = list(map(int, input().split()))

    def nextPermutation(a):

        #뒤에서부터 감소수열 끝나는 점 바로 앞의 값 찾기
        i = len(a)-1
        while i>0 and a[i-1] >= a[i]:
            i -= 1
        if i<= 0:
            return False

        #감소수열 중 바로 앞의 값보다 큰 값 찾고 swap
        j = len(a)-1
        while a[j] <= a[i-1]:
            j -= 1

        a[i-1],a[j] = a[j],a[i-1]

        #순열 뒤집기
        j = len(a)-1
        while i < j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

        return True

    if nextPermutation(checkList):
        print(' '.join(map(str, checkList)))
    else:
        print(-1)






