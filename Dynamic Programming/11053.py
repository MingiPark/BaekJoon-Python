if __name__ == "__main__":
    n = int(input())
    number = list(map(int, input().split(' ')))
    check = [0] * n

    for i in range(0, n):
        check[i] = 1
        for j in range(i):
            if number[j] < number[i] and check[j] + 1 > check[i]:
                check[i] = check[j] + 1

    print(max(check))
