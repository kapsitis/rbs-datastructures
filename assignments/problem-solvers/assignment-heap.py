import copy

def parentIdx(x):
    result = (x-1)//2
    return result

def leftChildIdx(x):
    return 2*x + 1

def rightChildIdx(x):
    return 2*x + 2

def insert(hh, xx):
    hh.append(xx)
    # set current to the just inserted element
    currIdx = len(hh) - 1
    while currIdx > 0 and hh[parentIdx(currIdx)] > hh[currIdx]:
        hh[parentIdx(currIdx)], hh[currIdx] = hh[currIdx], hh[parentIdx(currIdx)]
        currIdx = parentIdx(currIdx)

def removeTop(hh):
    result = hh[0]
    newTop = hh.pop()
    hh[0] = newTop
    currIdx = 0
    while currIdx <= len(hh) - 1:
        leftIdx = leftChildIdx(currIdx)
        rightIdx = rightChildIdx(currIdx)
        if leftIdx >= len(hh):
            break
        minIdx = leftIdx
        if rightIdx < len(hh) and hh[rightIdx] < hh[leftIdx]:
            minIdx = rightIdx
        if hh[currIdx] <= hh[minIdx]:
            break
        hh[currIdx], hh[minIdx] = hh[minIdx], hh[currIdx]
        currIdx = minIdx
    return result


def main():
    ourABCs = [332, 330, 314, 378, 319,
               320, 379, 333, 315, 321,
               380, 316, 381, 335, 381,
               100, 382, 322, 61, 336,
               337, 317, 383, 384, 385]

    ##a,b,c = [int(x) for x in input('Assignment 2021.5: Enter params a,b,c: ').split(' ')]
    ##print('a = {}, b = {}, c = {}'.format(a,b,c))

    for abc in ourABCs:
        a = (abc // 100) % 10
        b = (abc // 10) % 10
        c = abc % 10

        print("a,b,c = {},{},{}".format(a,b,c))
        print("========================================================")

        heap = [9, 23, 31, 35, 43, 61, 69, 49, 41, 53, 67, 75]
        HTP = copy.deepcopy(heap)
        while len(HTP) < 15:
            HTP.append('.')
        print('**(A)**')
        print('                           {}                            '.format(HTP[0]))
        print('            {}                           {}              '.format(HTP[1],HTP[2]))
        print('     {}            {}              {}            {}      '.format(HTP[3],HTP[4],HTP[5],HTP[6]))
        print('  {}    {}      {}     {}       {}     {}     {}     {}  '.format(
            HTP[7],HTP[8],HTP[9],HTP[10],HTP[11],HTP[12],HTP[13],HTP[14]))

        print()
        print('**(B)**')
        item = 10*a + 2*(b+c)
        insert(heap, item)
        HTP = copy.deepcopy(heap)
        while len(HTP) < 15:
            HTP.append('.')
        print('                           {}                            '.format(HTP[0]))
        print('            {}                           {}              '.format(HTP[1],HTP[2]))
        print('     {}            {}              {}            {}      '.format(HTP[3],HTP[4],HTP[5],HTP[6]))
        print('  {}    {}      {}     {}       {}     {}     {}     {}  '.format(
            HTP[7],HTP[8],HTP[9],HTP[10],HTP[11],HTP[12],HTP[13],HTP[14]))


        print()
        print('**(C)**')
        removeTop(heap)
        HTP = copy.deepcopy(heap)
        while len(HTP) < 15:
            HTP.append('.')
        print('                           {}                            '.format(HTP[0]))
        print('            {}                           {}              '.format(HTP[1],HTP[2]))
        print('     {}            {}              {}            {}      '.format(HTP[3],HTP[4],HTP[5],HTP[6]))
        print('  {}    {}      {}     {}       {}     {}     {}     {}  '.format(
            HTP[7],HTP[8],HTP[9],HTP[10],HTP[11],HTP[12],HTP[13],HTP[14]))
        print()
        print()

if __name__ == '__main__':
    main()
