#
# alds1 09c
#
import heapq


def main():
    S = []
    while True:
        cmd, *v = input().split()
        if cmd == "insert":
            heapq.heappush(S, (-1) * int(v[0]))
            pass
        elif cmd == "extract":
            print(heapq.heappop(S) * (-1))
        else:
            exit()


if __name__ == '__main__':
    main()
