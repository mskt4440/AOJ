#
# itp1 08b
#


def main():
    while True:
        l = input().rstrip()
        if l == "0":
            exit()
        else:
            s = 0
            for i in range(len(l)):
                s += int(l[i])
            print(s)


if __name__ == '__main__':
    main()
