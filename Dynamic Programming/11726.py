if __name__ == "__main__":
    n = int(input())
    answer = [0]*1001
    answer[0], answer[1], answer[2] = 0, 1, 2

    for i in range(3, n+1):
        answer[i] = answer[i-1] + answer[i-2]

    result = answer[n] % 10007

    print(result)