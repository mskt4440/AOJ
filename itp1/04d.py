#
# itp1 04d
#


def main():
    n = int(input())
    l = list(map(int, input().split()))
    print(min(l), max(l), sum(l))


if __name__ == '__main__':
    main()
