#
# itp1 07b
#


def main():
    while True:
        n, x = map(int, input().split())
        if n == 0 and x == 0:
            exit()
        r = 0
        for i in reversed(range(1, n+1)):
            for j in reversed(range(1, i)):
                if i + j < x and i + j + j > x:
                    r += 1
        print(r)


if __name__ == '__main__':
    main()
