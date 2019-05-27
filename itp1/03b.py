#
# itp1 03b
#


def main():
    for i in range(1, 10001):
        x = int(input())
        if x == 0:
            break
        else:
            print("Case %d: %d" % (i, x))


if __name__ == '__main__':
    main()
