#
# 5b
#

def main():
    while True:
        H, W = map(int, input().split())
        if H == W == 0:
            break
        for i in range(H):
            if i == 0 or i == H - 1:
                print("#" * W)
            else:
                print("#" + "." * (W-2) + "#")
        print()


if __name__ == '__main__':
    main()
