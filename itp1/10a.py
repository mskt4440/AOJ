#
# itp1 10a
#

import math


def main():
    x1, y1, x2, y2 = map(float, input().split())
    print(math.sqrt((x2-x1)**2 + (y2-y1)**2))


if __name__ == '__main__':
    main()
