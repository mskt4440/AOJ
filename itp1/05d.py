#
# 5d
#

def main():
    n = int(input())
    s = ""
    for i in range(1, n+1):
        x = i
        if x % 3 == 0 or x % 10 == 3:
            s += " " + str(i)
        else:
            x //= 10
            while x:
                if x % 10 == 3:
                    s += " " + str(i)
                    break
                x //= 10
    print(s)


if __name__ == '__main__':
    main()
