#
# 6c
#


def main():
    A = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]
    n = int(input())
    for i in range(n):
        b, f, r, v = map(int, input().split())
        A[b-1][f-1][r-1] += v
    for i in range(4):
        for j in range(3):
            print(" ", end="")
            print(*A[i][j])
        if i < 3:
            print("#" * 20)


if __name__ == '__main__':
    main()
