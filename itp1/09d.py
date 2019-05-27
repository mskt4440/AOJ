#
# itp1 09d
#


def main():
    s = input()
    q = int(input())
    for i in range(q):
        l = input().split()
        if l[0] == "print":
            print(s[int(l[1]):int(l[2])+1])
        elif l[0] == "reverse":
            s = s[0:int(l[1])] + s[int(l[1]):int(l[2]) +
                                   1][::-1] + s[int(l[2])+1:]
        else:
            s = s[0: int(l[1])] + l[3] + s[int(l[2])+1:]


if __name__ == '__main__':
    main()
