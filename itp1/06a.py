#
# 6a
#

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.reverse()
    print(*a)


if __name__ == '__main__':
    main()
