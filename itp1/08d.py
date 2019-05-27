#
# itp1 08d
#


def main():
    s = input().rstrip()
    p = input().rstrip()

    ret = "No"
    for i in range(len(p)):
        if i == 0 and p in s:
            ret = "Yes"
            break
        elif p[i:] == s[0:len(p)-i] and p[0:i] == s[i*(-1):]:
            ret = "Yes"
            break
    print(ret)


if __name__ == '__main__':
    main()
