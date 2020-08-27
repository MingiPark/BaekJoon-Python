if __name__ == "__main__":
    testCase = int(input())

    for _ in range(testCase):
        length = int(input())

        col1 = [0] + list(map(int, input().split(' ')))
        col2 = [0] + list(map(int, input().split(' ')))
        case = list(zip(col1, col2))

        value = [[0]*3 for _ in range(length+1)]

        for i in range(1, length+1):
            value[i][0] = max(value[i-1]) #안 뜯었을 경우
            value[i][1] = max(value[i-1][0], value[i-1][2]) + case[i][0] #위에 것을 뜯었을 경우
            value[i][2] = max(value[i-1][0], value[i-1][1]) + case[i][1] #아래 것을 뜯었을 경우

        ans = max(value[length])

        print(ans)
