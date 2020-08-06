#
# 7a
#

def main():
    while True:
        m, f, r = map(int, input().split())
        if m == f == r == -1:
            break
        elif (m == -1 or f == -1) or m+f < 30:
            print("F")
        elif m+f >= 80:
            print("A")
        elif m+f >= 65:
            print("B")
        elif m+f >= 50 or r >= 50:
            print("C")
        elif m+f >= 30:
            print("D")


if __name__ == '__main__':
    main()
