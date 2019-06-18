#
# alds1 06b
#


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def main():
    n = int(input())
    A = list(map(int, input().split()))
    q = partition(A, 0, len(A)-1)
    for i in range(q):
        print(A[i], end=" ")
    print("[{}]".format(A[q]), end=" ")
    for i in range(q+1, n):
        if i == n-1:
            print(A[i])
        else:
            print(A[i], end=" ")


if __name__ == '__main__':
    main()
