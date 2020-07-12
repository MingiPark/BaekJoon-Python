if __name__ == "__main__":
    person = [0]*9
    total = 0

    for i in range(9):
        a = int(input())
        person[i] = a
        total += a

    person.sort()

    for i in range(8):
        for j in range(i+1,9):
            if total - (person[i]+person[j]) == 100:
                for k in range(9):
                    if i == k or j == k:
                        continue
                    print(person[k])