import math


def domath(m, n, i, j):
    print 'j:', j, '  i:', i


def mysum(m, n):
    for j in range(1, n):
        for i in range(0, j + 1):
            domath(m, n, i, j)


def main():
    m = None
    n = 7
    mysum(m, n)

if __name__ == '__main__':
    main()
