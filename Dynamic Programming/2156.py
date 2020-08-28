if __name__ == "__main__":
    glass = int(input())
    quantity = [0] * (glass + 1)
    check = [0] * (glass + 1)

    for i in range(1, glass + 1):
        quantity[i] = int(input())

    check[1] = quantity[1]

    if glass >= 2:
        check[2] = quantity[1] + quantity[2]

    for j in range(3, glass + 1):

        check[j] = check[j-1]

        check[j] = max(check[j], check[j-2]+quantity[j])

        check[j] = max(check[j], check[j-3]+quantity[j]+quantity[j-1])

    print(check[glass])




