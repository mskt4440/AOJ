#
# 7c
#

def main():
    r, c = map(int, input().split())
    T = []
    S = [0 for _ in range(c+1)]
    for i in range(r):
        C = list(map(int, input().split()))
        C.append(sum(C))
        T.append(C)
    for i in range(r):
        for j in range(c+1):
            S[j] += T[i][j]
    T.append(S)
    for i in range(r+1):
        print(*T[i])


if __name__ == '__main__':
    main()
