if __name__ == "__main__":

    testCase = int(input())
    answer = [0] * 1000000

    answer[0], answer[1], answer[2] = 1, 1, 3
    result = [[1, 0, 0], [0, 1, 0], [1, 1, 1]]

    for i in range(3, 100000+1):
        count = 0

        temp = [0, 0, 0]
        temp[2] = result[0][0] + result[0][1]
        temp[1] = result[1][0] + result[1][2]
        temp[0] = result[2][1] + result[2][2]
        result[0] = result[1]
        result[1] = result[2]
        result[2] = temp
        answer[i] = sum(result[2]) % 1000000009

    for _ in range(testCase):
        value = int(input())
        print(answer[value-1])



