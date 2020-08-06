#
# 3d
#

def main():
    a, b, c = map(int, input().split())
    r = 0
    for i in range(a, b+1):
        if c % i == 0:
            r += 1
    print(r)


if __name__ == '__main__':
    main()
