#
# itp1 10d
#
import math


def main():
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    d1 = 0
    d2 = 0
    d3 = 0
    dm = []

    for i in range(n):
        d1 += abs(x[i] - y[i])
        d2 += abs(x[i] - y[i]) ** 2
        d3 += abs(x[i] - y[i]) ** 3
        dm.append(abs(x[i] - y[i]))

    print(d1)
    print(math.sqrt(d2))
    print(math.pow(d3, 1/3))
    print(max(dm))


if __name__ == '__main__':
    main()
