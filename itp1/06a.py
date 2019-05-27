#
# itp1 06a
#


def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.reverse()

    for i in range(n):
        if i >= 1:
            print(" ", end="")
        print(l[i], end="")
    print()


if __name__ == '__main__':
    main()
