#
# itp1 08c
#


def main():
    import sys

    R = "abcdefghijklmnopqrstuvwxyz"
    A = [0] * 26
    T = sys.stdin.read()

    for i in range(len(T)):
        for j, w in enumerate(R):
            if T[i] == w or T[i] == w.upper():
                A[j] += 1
                break


for i in range(26):
    print("{0} : {1}".format(R[i], A[i]))


if __name__ == '__main__':
    main()
