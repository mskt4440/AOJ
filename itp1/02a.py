#
# itp1 02a
#


def main():
    a, b = map(int, input().split())

    if a > b:
        print("a > b")
    elif a < b:
        print("a < b")
    else:
        print("a == b")


if __name__ == '__main__':
    main()
