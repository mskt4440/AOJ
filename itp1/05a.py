#
# itp1 05a
#


def main():
    while True:
        h, w = map(int, input().split())
        if h == 0 and w == 0:
            break
        else:
            for i in range(h):
                print("#" * w)
            print()


if __name__ == '__main__':
    main()
