#
# alds1 04b
#


def main():
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    q = int(input())
    t = list(map(int, input().split()))
    ans = 0
    for i in range(q):
        l = 0
        h = n
        m = (l + n) // 2
        while l < h:
            if t[i] == s[m]:
                ans += 1
                break
            elif t[i] < s[m]:
                h = m
            else:
                l = m + 1
            m = (l + h) // 2
    print(ans)


if __name__ == '__main__':
    main()
