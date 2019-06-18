#
# alds1 05a
#


def solve(m, a, n, i):
    if m == 0:
        return True
    if i >= n:
        return False
    return solve(m, a, n, i+1) or solve(m-a[i], a, n, i+1)


def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    M = list(map(int, input().split()))
    for m in M:
        if m < min(a) or m > sum(a):
            print("no")
        elif solve(m, a, n, 0):
            print("yes")
        else:
            print("no")


if __name__ == '__main__':
    main()
