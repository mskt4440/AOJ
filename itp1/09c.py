#
# itp1 09c
#


def main():
    a = 0
    b = 0
    n = int(input())
    for i in range(n):
        l = input().split()
        if l[0] == l[1]:
            a += 1
            b += 1
        elif l[0] > l[1]:
            a += 3
        else:
            b += 3
    print(a, b)


if __name__ == '__main__':
    main()
