#
# alds1 03b
#


def main():
    n, q = map(int, input().split())
    queue = []
    for i in range(n):
        name, time = input().split()
        time = int(time)
        queue.append([name, time])

    t = 0
    while queue:
        process = queue.pop(0)
        if process[1] > q:
            t += q
            queue.append([process[0], process[1] - q])
        else:
            t += process[1]
            print("{} {}".format(process[0], t))


if __name__ == '__main__':
    main()
