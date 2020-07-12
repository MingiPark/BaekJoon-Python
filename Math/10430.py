if __name__ == '__main__':
    inputValue = input()
    input = inputValue.split(" ")
    input = list(map(int, input))

    print((input[0] + input[1])%input[2])
    print(((input[0]%input[2])+(input[1]%input[2]))%input[2])
    print((input[0]*input[1])%input[2])
    print(((input[0]%input[2])*(input[1]%input[2]))%input[2])
