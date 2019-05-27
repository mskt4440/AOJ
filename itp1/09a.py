#
# itp1 09a
#


def main():
    W = input()
    ret = 0
    flag = 0
    while flag == 0:
        L = input().split()
        for S in L:
            if S == "END_OF_TEXT":
                flag = 1
                break
            elif S.upper() == W.upper():
                ret += 1

    print(ret)


if __name__ == '__main__':
    main()
