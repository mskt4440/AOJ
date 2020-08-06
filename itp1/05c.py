#
# 5c
#

def main():
    while True:
        H, W = map(int, input().split())
        if H == W == 0:
            break
        for i in range(H):
            s = ""
            if i % 2 == 1:
                for j in range(W):
                    if j % 2 == 0:
                        s += "."
                    else:
                        s += "#"
                print(s)
            else:
                for j in range(W):
                    if j % 2 == 0:
                        s += "#"
                    else:
                        s += "."
                print(s)
        print()


if __name__ == '__main__':
    main()
