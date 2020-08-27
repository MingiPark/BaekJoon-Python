if __name__ == "__main__":
    n = int(input())
    list = [0]*(90+1)
    list[0], list[1], list[2] = 0, 1, 1
    for i in range(3, 90+1):
        list[i] = list[i-1] + list[i-2]

    print(list[n])
