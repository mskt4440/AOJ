#
# itp1 02d
#


def main():
    w, h, x, y, r = map(int, input().split())

    if x-r < 0 or y-r < 0 or x+r > w or y+r > h:
        print("No")
    else:
        print("Yes")


if __name__ == '__main__':
    main()
