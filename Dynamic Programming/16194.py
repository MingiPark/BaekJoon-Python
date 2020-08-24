if __name__ == "__main__":
    card = int(input())
    price = [0] + list(map(int, input().split()))
    result = [-1] * (card+1)
    result[0] = 0

    for i in range(1, card+1):
        for j in range(1, i+1):
            if result[i] == -1 or result[i] > result[i-j] + price[j]:
                result[i] = result[i-j] + price[j]

    print(result[card])

