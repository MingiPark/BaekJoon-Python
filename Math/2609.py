if __name__ == "__main__":
    a,b = map(int,input().split())

    def gcd(a,b):
        if b==0:
            return a
        else:
            return gcd(b,a%b)

    def lsm(a,b):
        return int(a*b / gcd(a,b))

    print(gcd(a,b))
    print(lsm(a,b))