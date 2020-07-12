if __name__== "__main__":
    count = int(input())
    answer = 0

    for i in range(count):
        a = int(input())
        answer = 0
        for l1 in range(1,4):
            if l1 == a:
                answer += 1
            for l2 in range(1,4):
                if l1 + l2 == a:
                    answer += 1
                for l3 in range(1,4):
                    if l1 + l2 + l3 == a:
                        answer += 1
                    for l4 in range(1, 4):
                        if l1 + l2 + l3 + l4 == a:
                            answer += 1
                        for l5 in range(1, 4):
                            if l1 + l2 + l3 + l4 + l5 == a:
                                answer += 1
                            for l6 in range(1, 4):
                                if l1 + l2 + l3 + l4 + l5 + l6 == a:
                                    answer += 1
                                for l7 in range(1, 4):
                                    if l1 + l2 + l3 + l4 + l5 + l6 + l7 == a:
                                        answer += 1
                                    for l8 in range(1, 4):
                                        if l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 == a:
                                            answer += 1
                                        for l9 in range(1, 4):
                                            if l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9 == a:
                                                answer += 1
                                            for l10 in range(1, 4):
                                                if l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9 + l10 == a:
                                                    answer += 1
        print(answer)

