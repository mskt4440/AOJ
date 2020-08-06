#
# 6b
#

def main():
    n = int(input())
    c = []
    for i in range(n):
        m, r = input().split()
        r = int(r)
        c.append([m, r])
    for M in ["S", "H", "C", "D"]:
        for R in range(1, 14):
            for i in range(n):
                if c[i] == [M, R]:
                    break
            else:
                print(*[M, R])


if __name__ == '__main__':
    main()
