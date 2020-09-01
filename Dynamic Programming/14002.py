if __name__ == "__main__":
    n = int(input())
    value = list(map(int, input().split(' ')))
    check = [0]*n # 증가 하는 수열의 크기를 찾기 위한 List
    change = [-1]*n # 해당 부분의 값이 어떤 부분에 의해서 값이 바뀌었는지 표시하는 List

    for i in range(n):
        check[i] = 1
        for j in range(i):
            if value[j] < value[i] and check[j]+1 > check[i]:
                check[i] = check[j] + 1
                change[i] = j # 여기서 기록

    print(max(check))

    ans = []
    max_idx = check.index(max(check))
    while max_idx != -1:
        ans.append(value[max_idx]) # 값을 저장
        max_idx = change[max_idx] # 해당 부분으로 이동
    ans.reverse() # 큰 수부터 저장하므로 마지막에 전체 순서를 뒤집어준다.

    print(' '.join(map(str, ans)))