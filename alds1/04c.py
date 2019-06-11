#
# alds1 04c
#


def main():
    n = int(input())
    d = set()
    for i in range(n):
        c, w = input().split()
        if c == "insert":
            d.add(w)
        else:
            if w in d:
                print("yes")
            else:
                print("no")


if __name__ == '__main__':
    main()
