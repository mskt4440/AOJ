#
# alds1 03c
#
from collections import deque


def main():
    ans = deque()
    n = int(input())
    for i in range(n):
        c = input()
        if c == "deleteFirst":
            ans.popleft()
        elif c == "deleteLast":
            ans.pop()
        else:
            c, x = c.split()
            if c == "insert":
                ans.insert(0, x)
            else:
                try:
                    ans.remove(x)
                except ValueError:
                    pass
    print(*ans)


if __name__ == '__main__':
    main()
