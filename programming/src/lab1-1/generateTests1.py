import random

#9
#1 2 0 3 0 0 4 0 5

def main():




    # Test07: All
    lines = list()
    for i in range(0,3):
        vv = list()
        for j in range(0,5):
            vv.append(random.randint(-50,0))
        lines.append(' '.join(list(map(lambda x: str(x), vv))))
#    with open('input1-07.txt', mode='w') as myfile:
#        myfile.write('\n'.join(lines))
#        myfile.write('\n')


    # Test08: All negative
    lines = list()
    for i in range(0,3):
        vv = list()
        for j in range(0,5):
            vv.append(random.randint(-2,-1))
        lines.append(' '.join(list(map(lambda x: str(x), vv))))
#    with open('input1-08.txt', mode='w') as myfile:
#        myfile.write('\n'.join(lines))
#        myfile.write('\n')


    # Test09: All negative - and very different
    lines = list()
    for i in range(0,3):
        vv = list()
        for j in range(0,5):
            vv.append(random.randint(-1000000000, -1))
        lines.append(' '.join(list(map(lambda x: str(x), vv))))
#    with open('input1-09.txt', mode='w') as myfile:
#        myfile.write('\n'.join(lines))
#        myfile.write('\n')

    # Test10: All very negative
    lines = list()
    for i in range(0,3):
        vv = list()
        for j in range(0,5):
            vv.append(random.randint(-1000000000, -999999994))
        lines.append(' '.join(list(map(lambda x: str(x), vv))))
    #with open('input1-10.txt', mode='w') as myfile:
    #    myfile.write('\n'.join(lines))


if __name__ == '__main__':
    main()