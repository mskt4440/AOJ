#
# 8a
#

def main():
    while True:
        x = input()
        if x == "0":
            break
        r = 0
        for i in range(len(x)):
            r += int(x[i])
        print(r)


if __name__ == '__main__':
    main()
