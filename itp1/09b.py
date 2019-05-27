#
# itp1 09b
#


def main():
    ret = []
    while True:
        L = input()
        if L == "-":
            break
        elif L.isalpha():
            M = int(input())
            for i in range(M):
                H = int(input())
                L = L[H:] + L[:H]
            ret.append(L)

    for r in ret:
        print(r)


if __name__ == '__main__':
    main()
