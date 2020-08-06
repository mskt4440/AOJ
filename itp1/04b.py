#
# 4b
#
import math


def main():
    r = float(input())
    S = r * r * math.pi
    L = 2 * r * math.pi
    print(f"{S:.6f} {L:.6f}")


if __name__ == '__main__':
    main()
