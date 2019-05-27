#
# itp1 07d
#


def main():
    n, m, l = map(int, input().split())
    a = [[0] * n for i in range(n)]
    b = [[0] * l for i in range(m)]
    c = [[0] * l for i in range(n)]

    for i in range(n):
        a[i] = list(map(int, input().split()))
    for i in range(m):
        b[i] = list(map(int, input().split()))

    for x in range(n):
        for y in range(l):
            for z in range(m):
                c[x][y] += a[x][z] * b[z][y]

    for x in range(n):
        for y in range(l):
            if y == l-1:
                print(c[x][y])
            else:
                print(c[x][y], end=" ")


if __name__ == '__main__':
    main()
