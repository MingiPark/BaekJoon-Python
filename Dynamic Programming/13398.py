if __name__ == "__main__":
    n = int(input())
    value = list(map(int, input().split(' ')))
    left = [0]*n
    right = [0]*n

    #오른쪽 방향으로서의 최댓값 구하기(i번째 index를 마지막 원소로 갖는)
    for i in range(n):
        right[i] = value[i]
######missing part######
        if i == 0:
            continue
########################
        if right[i] < right[i-1] + value[i]:
            right[i] = right[i-1] + value[i]

    ans = 0
    ans = max(right)

    #왼쪽(역) 방향으로서의 최댓값 구하기(j번째 index를 시작 원소로 갖는)
    for j in range(n-1, -1, -1):
        left[j] = value[j]
        if j <= n-2:
            if left[j] < left[j+1] + value[j]:
                left[j] = left[j+1] + value[j]

    #k번째 원소를 삭제한경우의 최댓값 찾기
    for k in range(1, n-1):
        if left[k+1] + right[k-1] > ans:
            ans = left[k+1] + right[k-1]

    print(ans)
