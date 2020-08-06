#
# 7b
#

def main():
    while True:
        n, x, = map(int, input().split())
        if n == x == 0:
            break
        ans = 0
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                if j+1 <= x - i - j <= n:
                    ans += 1
        print(ans)


if __name__ == '__main__':
    main()
