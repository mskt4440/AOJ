#
# itp1 07c
#


def main():
    r, c = map(int, input().split())
    x = []
    for i in range(r):
        l = list(map(int, input().split()))
        l.append(sum(l))
        x.append(l)
    x.append([0] * (c+1))

    for i in range(r+1):
        for j in range(c+1):
            if j == c:
                print(x[i][j])
            else:
                print(x[i][j], end=" ")
            if i < r+1:
                x[r][j] += x[i][j]


if __name__ == '__main__':
    main()
