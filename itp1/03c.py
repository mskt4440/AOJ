#
# itp1 03c
#


def main():
    for i in range(10000):
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        else:
            if a < b:
                print(a, b)
            else:
                print(b, a)


if __name__ == '__main__':
    main()
