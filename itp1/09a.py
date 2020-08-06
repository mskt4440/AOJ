#
# 9a
#

def main():
    W = input().lower()
    T = []
    while True:
        t = input()
        if t == "END_OF_TEXT":
            break
        T += list(t.lower().split())

    ret = 0
    for i in range(len(T)):
        if T[i] == W:
            ret += 1
    print(ret)


if __name__ == '__main__':
    main()
