#
# itp1 03d
#


def main():
    a, b, c = map(int, input().split())
    ret = 0
    for i in range(a, b+1):
        if c % i == 0:
            ret += 1
    print(ret)


if __name__ == '__main__':
    main()
