#
# 1d
#

def main():
    S = int(input())
    h = S // 60 // 60
    m = S // 60 % 60
    s = S % 60
    print(f"{h}:{m}:{s}")


if __name__ == '__main__':
    main()
