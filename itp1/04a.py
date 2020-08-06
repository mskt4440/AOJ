#
# 4a
#

def main():
    a, b = map(int, input().split())
    d = a // b
    r = a % b
    f = a / b
    print(f"{d} {r} {f:.5f}")


if __name__ == '__main__':
    main()
