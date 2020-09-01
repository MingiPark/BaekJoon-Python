if __name__ =="__main__":
    n = int(input())
    value = list(map(int, input().split(' ')))
    ans = [0]*n

    for i in range(0, n):
        ans[i] = value[i]
        if ans[i-1] + value[i] > ans[i]:
            ans[i] = ans[i-1] + value[i]

    print(max(ans))