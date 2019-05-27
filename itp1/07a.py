#
# itp1 07a
#


def main():
    while True:
        m, f, r = map(int, input().split())
        if m == -1 and f == -1 and r == -1:
            exit()
        ret = ""
        s = m + f
        if m == -1 or f == -1 or s < 30:
            ret = "F"
        elif s >= 80:
            ret = "A"
        elif s >= 65:
            ret = "B"
        elif s >= 50:
            ret = "C"
        elif r >= 50:
            ret = "C"
        else:
            ret = "D"

        print(ret)


if __name__ == '__main__':
    main()
