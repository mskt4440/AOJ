#
# itp1 04c
#


def main():
    while True:
        line = input().split()
        a = int(line[0])
        op = line[1]
        b = int(line[2])

        if op == "+":
            print(a + b)
        elif op == "-":
            print(a - b)
        elif op == "*":
            print(a * b)
        elif op == "/":
            print(a // b)
        else:
            break


if __name__ == '__main__':
    main()
