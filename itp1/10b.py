#
# itp1 10b
#
import math


def main():
    a, b, c = map(int, input().split())

    d = math.radians(c)
    print(a * b * math.sin(d) / 2)
    print(a + b + math.sqrt(a**2+b**2-2*a*b*math.cos(d)))
    print(b*math.sin(d))


if __name__ == '__main__':
    main()
