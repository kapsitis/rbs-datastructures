## Cyclic Polynomial function
import numpy as np

# get np.uint8 argument, rotate it to the right by k positions, return as np.uint8
def rotate(num, k):
    k = k % 8
    uu = np.right_shift(num, k)
    vv = np.bitwise_and(np.left_shift(num, 8-k), 255)
    #print('uu = {}'.format(np.binary_repr(uu, width=8)))
    #print('vv = {}'.format(np.binary_repr(vv, width=8)))
    ww = np.bitwise_xor(uu,vv)
    print('ww = {}'.format(np.binary_repr(ww, width=8)))
    return ww



def rollingHash(arg):
    result = np.uint8(0)
    n = len(arg)
    for i in range(0, n):
        x = np.uint8(ord(arg[i]))
        result = np.bitwise_xor(result,rotate(x, n - i - 1))

    print('bits = {}'.format(np.binary_repr(result, width=8)))
    print('h({}) = {}'.format(arg, result % 7))


def main():
    s1 = 'BOMB'
    rollingHash(s1)
    print()
    for i in range(0,8):
        rotate(np.uint8(ord('B')),i)


if __name__ == '__main__':
    main()

