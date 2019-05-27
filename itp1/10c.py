#
# itp1 10c
#
import math


def main():
    while True:
        n = int(input())
        if n == 0:
            exit()
        else:
            l = list(map(int, input().split()))
            ave = sum(l) / n
            S = 0
            for i in range(n):
                S += (l[i] - ave) ** 2
            S /= n
        print(math.sqrt(S))


if __name__ == '__main__':
    main()
