if __name__ == "__main__":
    n = int(input())
    d = [0]*(n+1)
    for i in range(1, n+1):
        d[i] = i
        j = 1
        while j*j <= i:
            if d[i] > d[i-j*j]+1:
                d[i] = d[i-j*j]+1
            j += 1
    print(d[n])

    """n = int(input())
    k = int(n/2)
    ans = n
    t = 0

    for i in range(1, k):
        if pow(i,2) < n:
            t = pow(i,2)
        elif pow(i, 2) == n:
            ans = 1 #제곱수의 경우

    for j in range(2, t):
        temp = 0
        save = n
        for m in range(j, 0, -1):
            while save - pow(m, 2) >= 0:
                save = save - pow(m, 2)
                temp += 1
        if save == 1:
            temp += 1
        if temp < ans:
            ans = temp

    print(ans)"""


