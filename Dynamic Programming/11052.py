if __name__ == "__main__":

    card = int(input())
    price = [0] + list(map(int, input().split()))
    result = [0]*(card+1)

    for i in range(1, card+1):
        for j in range(1, i+1):
            result[i] = max(result[i], result[i-j] + price[j])

    print(result[card])

    # card = int(input())
    # price = list(map(int, input().split()))
    # num = sorted(price, reverse=True)
    # print(num)
    #
    # j = 0
    # check1 = [0]*card
    # while j != card:
    #     for i in range(card):
    #         if j == card:
    #             break
    #         if num[j] == price[i]:
    #             check1[j] = i
    #             j += 1
    #
    # print(check1)
    # check2 = card
    # result = 0
    # i = 0
    #
    # while i != check2:
    #     if check2 == 0:
    #         break
    #     if check1[i] <= check2 and (check2 - check1[check1[i]]) > 0:
    #         if check2 < 0:
    #             check2 = card
    #             i = 0
    #         else:
    #             result = result + price[check1[i]]
    #             check2 = check2 - (check1[i] + 1)
    #             i += 1
    #
    #
    # print(result)

