if __name__ == "__main__":
    a = int(input())
    count = 0
    score = [0]*(a+1)

    #Top - Down
    def cal(x):
        if x == 1:
            return 0
        score[x] = cal(x-1) + 1

        if x % 2 == 0:
            temp = cal(int(x/2)) + 1
            if score[x] > temp:
                score[x] = temp

        if x % 3 == 0:
            temp = cal(int(x/3)) + 1
            if score[x] > temp:
                score[x] = temp

        return score[x]

    score[1] = 0

    #Bottom - Up - python 추천
    for i in range(2, a+1):
        score[i] = score[i-1] + 1
        if i % 2 == 0 and score[i] > score[int(i/2)] + 1:
            score[i] = score[int(i/2)] + 1
        if i % 3 == 0 and score[i] > score[int(i/3)] + 1:
            score[i] = score[int(i/3)] + 1

    cal(a)

    print(score[a])

