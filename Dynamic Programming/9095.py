if __name__ == '__main__':
    t = int(input())
    list = [0]*t

    for i in range(t):
        list[i] = int(input())

    answer = [0]*(max(list)+1)

    answer[0], answer[1], answer[2], answer[3] = 0, 1, 2, 4

    for j in range(4, max(list)+1):
        answer[j] = answer[j-1] + answer[j-2] + answer[j-3]

    for k in range(t):
        print(answer[list[k]])