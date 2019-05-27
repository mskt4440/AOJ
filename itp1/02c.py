#
# itp1 02c
#


def main():
    l = list(map(int, input().split()))
    l.sort()
    print(l[0], l[1], l[2])


if __name__ == '__main__':
    main()
