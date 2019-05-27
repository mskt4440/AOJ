#
# itp1 06d
#


def main():
    n, m = map(int, input().split())

    a = [0] * n
    b = [0] * m

    for i in range(n):
        a[i] = list(map(int, input().split()))

    for i in range(m):
        b[i] = int(input())

    for i in range(n):
        ret = 0
        for j in range(m):
            ret += a[i][j] * b[j]
        print(ret)


if __name__ == '__main__':
    main()
