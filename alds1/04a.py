#
# alds1 04a
#


def main():
    n = int(input())
    s = list(map(int, input().split()))
    q = int(input())
    t = list(map(int, input().split()))
    ans = 0
    for i in range(q):
        for j in range(n):
            if t[i] == s[j]:
                ans += 1
                break
    print(ans)


if __name__ == '__main__':
    main()
