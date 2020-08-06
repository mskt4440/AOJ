#
# 4d
#


def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(f"{min(a)} {max(a)} {sum(a)}")


if __name__ == '__main__':
    main()
