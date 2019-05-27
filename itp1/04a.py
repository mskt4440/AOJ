#
# itp1 04a
#


def main():
    a, b = map(int, input().split())
    print("%d %d %0.5f" % (a//b, a % b, a/b))


if __name__ == '__main__':
    main()
