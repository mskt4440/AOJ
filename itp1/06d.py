#
# 6d
#


def main():
    n, m = map(int, input().split())
    A = [[0 for i in range(m)] for j in range(n)]
    B = [0 for i in range(m)]
    C = [0 for i in range(n)]
    for i in range(n):
        A[i] = list(map(int, input().split()))
    for i in range(m):
        B[i] = int(input())

    for i in range(n):
        for j in range(m):
            C[i] += A[i][j] * B[j]
        print(C[i])


if __name__ == '__main__':
    main()
