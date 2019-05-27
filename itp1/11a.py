#
# itp1 11a
#


class Cube:
    def __init__(self, u, s, e, w, n, d):
        self.u = u
        self.s = s
        self.e = e
        self.w = w
        self.n = n
        self.d = d

    def rotate(self, dic):
        if dic == "N":
            tmp = self.u
            self.u = self.s
            self.s = self.d
            self.d = self.n
            self.n = tmp
        elif dic == "E":
            tmp = self.u
            self.u = self.w
            self.w = self.d
            self.d = self.e
            self.e = tmp
        elif dic == "W":
            tmp = self.u
            self.u = self.e
            self.e = self.d
            self.d = self.w
            self.w = tmp
        else:
            tmp = self.u
            self.u = self.n
            self.n = self.d
            self.d = self.s
            self.s = tmp


def main():
    u, s, e, w, n, d = map(int, input().split())
    O = input()

    cube = Cube(u, s, e, w, n, d)
    for i in range(len(O)):
        cube.rotate(O[i])
    print(cube.u)


if __name__ == '__main__':
    main()
